#!/usr/bin/env python3
"""Idempotent updater for the {c:<BPM> BPM, <M:SS>} header comment.

For every *.chordpro file in the repo root:
- Strips every existing BPM comment line ({c: ... BPM, ...}), every obsolete
  standalone {c:Tempo ...} / {c:Duration ...} line, wherever they occur.
- If the file has both {metronome:} and {duration:}, inserts
  {c: <BPM> BPM, <M:SS>} into the header immediately before the {midi:} line
  (creating a default {midi:} line if the header has none).
- Files missing either datum get no comment and no default insertion.

Safe to run repeatedly.
"""
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_MIDI = "{midi: CC0.0@2, PC10@2}"

DIRECTIVE_RE = re.compile(r'^\{\s*([A-Za-z_]+)\s*:\s*(.*?)\}\s*$')
DROP_RE = re.compile(r'^\{c\s*:\s*(?:Tempo\b|Duration\b|.*BPM,)', re.IGNORECASE)


def header_extent(lines):
    """Index of first line after the leading directive block."""
    i = 0
    n = len(lines)
    while i < n:
        if DIRECTIVE_RE.match(lines[i].strip()):
            i += 1
        elif lines[i].strip() == "" and i > 0 and DIRECTIVE_RE.match(lines[i - 1].strip()):
            i += 1  # blank separators inside header region
        else:
            break
    return i


def process(path, dry=False):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    end = header_extent(lines)
    header, body = lines[:end], lines[end:]

    metronome = duration = midi = None
    new_header = []
    for raw in header:
        s = raw.strip()
        m = DIRECTIVE_RE.match(s)
        if DROP_RE.match(s):
            continue  # strip old BPM/Tempo/Duration comments
        if m:
            key, val = m.group(1).lower(), m.group(2).strip()
            if key == "metronome" and val:
                metronome = val
            elif key == "duration" and val:
                duration = val
            elif key == "midi" and midi is None:
                midi = raw.rstrip()
        new_header.append(raw.rstrip())

    changed = new_header != [l.rstrip() for l in header]

    have_data = metronome is not None and duration is not None
    if have_data:
        comment = "{c: %s BPM, %s}" % (metronome, duration)
        if not any(l.strip() == comment for l in new_header):
            if midi is None:
                midi = DEFAULT_MIDI
            idx = new_header.index(midi)
            new_header.insert(idx, comment)
            changed = True

    # Trim trailing blank lines from the whole file.
    all_lines = new_header + body
    while all_lines and all_lines[-1] == "":
        all_lines.pop()
        changed = True

    content = "\n".join(all_lines) + "\n"
    if changed and not dry:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    return changed, have_data


def main():
    dry = "--dry-run" in sys.argv
    changed = skipped = 0
    for path in sorted(glob.glob(os.path.join(REPO, "*.chordpro"))):
        ch, have = process(path, dry)
        if ch and have:
            changed += 1
        elif not have:
            skipped += 1
    print("updated:", changed, "no-data files:", skipped)


if __name__ == "__main__":
    main()
