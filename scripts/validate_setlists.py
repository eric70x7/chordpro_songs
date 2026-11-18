"""Validate .lst setlist files against {t:} titles in chordpro files.

Checks:
  1. Every entry in every .lst file (after the title line) must reference a
     song title that exactly matches the {t:} header of a .chordpro/.pro file.
     Unicode punctuation variants (curly quotes, dashes) are normalized
     before comparison, so entries must differ in actual characters to fail.
  2. Legacy {title:} headers and files with no title header are reported as
     warnings, not errors.

Exit codes:
  0 = all entries resolvable
  1 = validation failures (unmatched titles)
"""

import difflib
import re
import sys
from pathlib import Path

TITLE_RE = re.compile(r"^\{t:\s*(.+?)\s*\}", re.MULTILINE)
LEGACY_TITLE_RE = re.compile(r"^\{title:\s*(.+?)\s*\}", re.MULTILINE)
ARTIST_RE = re.compile(r"^\{(?:st|artist):\s*(.+?)\s*\}", re.MULTILINE)

# Unicode punctuation commonly varies between sources; normalize it.
NORMALIZE_MAP = {
    "\u2018": "'",
    "\u2019": "'",
    "\u02bc": "'",
    "\u2032": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u00a0": " ",
    "\u2013": "-",
    "\u2014": "-",
}


def normalize(s: str) -> str:
    for k, v in NORMALIZE_MAP.items():
        s = s.replace(k, v)
    return re.sub(r"\s+", " ", s).strip().lower()


def parse_entry(line: str) -> tuple[str, str]:
    """Split '<Title> - <Artist>' using the LAST ' - ' as separator."""
    idx = line.rfind(" - ")
    if idx == -1:
        raise ValueError(f"entry has no ' - ' separator: {line!r}")
    return line[:idx].strip(), line[idx + 3:].strip()


def collect_titles(root: Path):
    """Return ({normalized_title: (display_title, artist, filename)},
    legacy_warnings, missing_warnings)."""
    titles = {}
    legacy = []
    missing = []
    for pattern in ("*.chordpro", "*.pro"):
        for path in sorted(root.rglob(pattern)):
            try:
                text = path.read_text(encoding="utf-8")
            except Exception as e:
                missing.append((path.name, f"unreadable: {e}"))
                continue
            m = TITLE_RE.search(text)
            if m:
                title = m.group(1)
            else:
                lm = LEGACY_TITLE_RE.search(text)
                if lm:
                    legacy.append((path.name, lm.group(1)))
                    title = lm.group(1)
                else:
                    missing.append((path.name, "no {t:} header"))
                    continue
            am = ARTIST_RE.search(text)
            artist = am.group(1) if am else "?"
            titles[normalize(title)] = (title, artist, path.name)
    return titles, legacy, missing


def validate_setlists(root: Path, titles: dict):
    errors = []
    lst_files = sorted(root.rglob("*.lst"))
    if not lst_files:
        print("::warning::no .lst files found")
    for lst in lst_files:
        rel = lst.relative_to(root)
        lines = lst.read_text(encoding="utf-8").splitlines()
        if not lines or not lines[0].strip():
            errors.append((rel, 0, "missing title line"))
            continue
        for lineno, line in enumerate(lines[1:], start=2):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                song, _artist = parse_entry(line)
            except ValueError as e:
                errors.append((rel, lineno, str(e)))
                continue
            key = normalize(song)
            if key in titles:
                t, a, fname = titles[key]
                if song != t:
                    errors.append(
                        (rel, lineno,
                         f"'{song}' resolves to '{t}' ({fname}) but spelling/"
                         f"casing differs; setlists must use the exact repo title")
                    )
            else:
                close = difflib.get_close_matches(
                    key, titles.keys(), n=1, cutoff=0.75
                )
                hint = f" (closest: '{titles[close[0]][0]}')" if close else ""
                errors.append(
                    (rel, lineno,
                     f"'{song}' not found in any chordpro file{hint}")
                )
    return errors


def main():
    root = Path(".")
    titles, legacy, missing = collect_titles(root)

    print(f"Indexed {len(titles)} song titles from chordpro files.")
    for name, title in legacy:
        print(f"::warning file={name}::legacy {{{{title:}}}} header "
              f"(title: {title}); consider converting to {{{{t:}}}}")
    for name, reason in missing:
        print(f"::warning file={name}::{reason}")

    errors = validate_setlists(root, titles)

    if errors:
        print(f"\n{len(errors)} problem(s) found:\n")
        for rel, lineno, msg in errors:
            print(f"  {rel}:{lineno}: {msg}")
        sys.exit(1)

    print("\nAll .lst entries resolve to chordpro titles. OK")


if __name__ == "__main__":
    main()
