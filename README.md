# chordpro_songs

# Preferred ChordPro Format Settings

- **Header**:
  - `{t: <Song Title>}`: Song title.
  - `{st: <Artist Name>}`: Artist name.
  - `{key: <Key>}`: Key of the song (e.g., G, Dm).
  - `{metronome: xxx}`: Tempo in beats per minute (BPM).
  - `{duration: m:ss}`: Song duration in minutes and seconds.
  - `{ipodid: <ID>}`: Custom metadata, included if provided.
  - `{tag: Whiskey Lizard}`: Custom tag, included if provided or for consistency with previous submissions.

- **Synopsis**:
  - Placed at the top, before song sections.
  - Includes `{c:Tempo XXX}` as the first comment, where XXX is the tempo in BPM.
  - Includes `{c:<Section Name>}` for each section (e.g., `{c:Intro}`, `{c:Verse 1}`, `{c:Chorus}`).
  - For sections with lyrical content, the first line of lyrics is placed on the same line, immediately after the closing curly brace (e.g., `{c:Verse 1} Well, the whole town's talkin', 'bout the line I'm walkin'`).
  - For sections without lyrics (e.g., Intro, Solo), only the section name is included (e.g., `{c:Intro}`).
  - Preserves any additional comments provided (e.g., `{c: SOLO}`, `{c: SCRAPE}`).

- **Section Structure**:
  - Non-chorus sections use `{sop: <Section Name>}` to start and `{eop}` to end (e.g., Verse, Intro, Bridge, Solo, Interlude, Outro).
  - Chorus sections use `{soc}` to start and `{eoc}` to end.
  - Chords are placed in `[brackets]` above the corresponding lyrics.
  - Duplicate chord progressions are omitted within the same section if unchanged from the previous line.
  - Instrumental measures in sections without lyrics use `- - -` instead of `|`.
  - Long lyric lines are preserved, maintaining original line breaks where provided.
  - Stylistic elements (e.g., contractions like "’bout", "gimme", or "MoMoMony") are preserved exactly as provided.

- **Additional Notes**:
  - Content type is `text/plain` for ChordPro files.
  - Sections are labeled as provided (e.g., `{c: SAX SOLO}`, `{c:STOP}`), with interpretation based on content if ambiguous (e.g., `{c: Verse Chorus}` as Verse or Chorus).
  - If no `{ipodid}` or `{tag: Whiskey Lizard}` is provided, `{tag: Whiskey Lizard}` may be included for consistency with previous submissions unless specified otherwise.
  - Key, metronome, and duration are sourced from the input or verified via external sources (e.g., SongBPM, Musicstax, Apple Music) if not provided.