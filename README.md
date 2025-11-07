# Current ChordPro Formatting Rules

## Header
- `{t: <Song Title>}`: Song title.
- `{st: <Artist Name>}`: Artist name.
- `{key: <Key>}`: Key of the song (e.g., G, Em).
- `{metronome: <XXX>}`: Tempo in BPM (sourced/verified via SongBPM or similar).
- `{duration: <M:SS>}`: Song duration (sourced/verified).
- `{ipodid: <ID>}`: **Only** if explicitly provided in input.

## Synopsis (placed at top, before sections)
- `{c:Tempo XXX}`: First line, XXX = BPM.
- One `{c:<Section Name>}` per section (e.g., `{c:Intro}`, `{c:Verse 1}`, `{c:Chorus}`).
- For **lyrical sections**: first lyric line **immediately after** closing brace on same line:
  - e.g., `{c:Verse 1} Well, the whole town's talkin', 'bout the line I'm walkin'`
- For **non-lyrical sections** (Intro, Solo, etc.): only section name:
  - e.g., `{c:Intro}`
- Preserve additional comments exactly (e.g., `{c: SOLO}`, `{c: SCRAPE}`).

## Section Structure
- **Non-chorus**: `{sop: <Section Name>}` → `{eop}`
- **Chorus**: `{soc}` → `{eoc}`
- **Chords on separate line above lyrics**, in `[brackets]`.
- **Chords and lyrics strictly separated** — never on same line.
- **Duplicate chord progressions omitted** within same section if unchanged.
- **Instrumental measures**: use chords only (no `- - -` unless specified).
- **Preserve original line breaks** in lyrics.
- **Preserve stylistic text** exactly (e.g., `dre__ams`, `’bout`, `groovey`, `Borealice`).

## Alignment & Spacing
- Chords aligned **above** corresponding lyric syllables/words using spaces.
- Example:

[G5]     [A5]      [A5]
Well we had a lot of luck on Venus

## Additional Rules
- **Content type**: `text/plain`
- **Section labels**: use exactly as provided; interpret ambiguous ones by content.
- **Do NOT include** `{tag: Whiskey Lizard}` unless explicitly in input.
- **Key, BPM, duration**: source from input or verify via external (SongBPM, Musicstax, etc.).
- **Outro/Fade Out**: treated as separate sections if labeled.