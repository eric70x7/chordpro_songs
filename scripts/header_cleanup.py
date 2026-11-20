#!/usr/bin/env python3
"""Header cleanup for chordpro song files.

For every *.chordpro file in the repo root:
- Normalizes directive spacing ({key:F} -> {key: F}).
- Converts {artist: ...} to {st: ...}.
- Moves all {midi: ...} and {tag: ...} lines (wherever they occur) into the header.
- Rebuilds the header in canonical order:
    {t}, {st}, {key}, {metronome}, {duration}, tags, midi, {ipodid}
- Deduplicates identical midi/tag directives (e.g. duplicated midi lines).
- Preserves unusual midi values (manual patches like CC0.6@2, PC120@2) as-is.
- Adds the default {midi: CC0.0@2, PC10@2} if a file has no midi directive.
- Leaves all {c: ...} comment lines and structural markers untouched, in place.
- Trims trailing blank lines.

Usage: python3 scripts/header_cleanup.py [--dry-run]
"""
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_MIDI = "{midi: CC0.0@2, PC10@2}"

DIRECTIVE_RE = re.compile(r'^\{\s*([A-Za-z_]+)\s*:?\s*(.*?)\}\s*$')
MOVE_KEYS = {"midi", "tag"}
HEADER_ORDER = ["t", "st", "key", "metronome", "duration"]


def norm_directive(key, value):
    value = value.strip()
    if value:
        return "{%s: %s}" % (key, value)
    return "{%s: }" % key


def process(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    collected = {k: [] for k in HEADER_ORDER + ["tag", "midi", "ipodid"]}
    body = []

    ipod_entries = []
    body = []
    in_leading_header = True
    for raw in lines:
        m = DIRECTIVE_RE.match(raw.strip())
        if m:
            key = m.group(1).lower()
            if key == "title" and in_leading_header and m.group(2).strip() == "":
                # Drop empty {title:} directives.
                continue
            if key == "artist":
                key = "st"
            if in_leading_header and key in collected:
                entry = norm_directive(key, m.group(2))
                if entry not in collected[key]:
                    collected[key].append(entry)
                continue
            if key in MOVE_KEYS:
                entry = norm_directive(key, m.group(2))
                if entry not in collected[key]:
                    collected[key].append(entry)
                continue
        if in_leading_header and raw.strip() == "":
            # Blank line before the first song text: still part of the header scan.
            continue
        in_leading_header = False
        body.append(raw.rstrip())

    # Trim trailing blank lines from body.
    while body and body[-1] == "":
        body.pop()

    # Ensure at least one midi directive.
    if not collected["midi"]:
        collected["midi"] = [DEFAULT_MIDI]

    content_parts = []
    for key in HEADER_ORDER:
        content_parts.extend(collected[key])
    content_parts.extend(collected["tag"])
    content_parts.extend(collected["midi"])
    content_parts.extend(collected["ipodid"])

    # Keep exactly one blank line between header and body.
    if body and body[0] != "":
        body = [""] + body
    elif body and body[0] == "":
        while len(body) > 1 and body[0] == "" and body[1] == "":
            body.pop(0)

    return "\n".join(content_parts + body) + "\n"


def main():
    dry = "--dry-run" in sys.argv
    changed = 0
    for path in sorted(glob.glob(os.path.join(REPO, "*.chordpro"))):
        new = process(path)
        with open(path, encoding="utf-8") as f:
            old = f.read()
        if new != old:
            changed += 1
            print("changed:", os.path.basename(path))
            if not dry:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new)
    print("total changed:", changed)


if __name__ == "__main__":
    main()
