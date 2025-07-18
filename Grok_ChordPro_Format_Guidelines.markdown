# ChordPro Format Guidelines

These guidelines outline the preferred ChordPro format for structuring and presenting song chord sheets, based on specific formatting preferences. The format is designed to be clear, consistent, and compatible with standard ChordPro conventions, with details for a song structure synopsis, metronome (tempo), duration, and section handling.

## Synopsis
- **Placement**: Include a synopsis at the top of the file, after the header but before the first section, using ChordPro comments (`{c:XXXXX}`).
- **Content**: List each section of the song in the order they appear, with one comment per section, using the exact section names as provided (e.g., `{c:Intro}`, `{c:Verse 1}`, `{c:Chorus}`, `{c:Break}`, `{c:Solo}`, `{c:Outro}`, `{c:Fade Out}`). For sections with lyrics, place the first line of lyrics on the same line as the comment, after the closing curly brace, separated by a space (e.g., `{c:Verse 1} I got my first real sixstring`). For sections without lyrics (e.g., Intro, Break, or purely instrumental Solos), include only the section name in the comment (e.g., `{c:Intro}`).
- **Example**:
  ```
  {c:Intro}
  {c:Verse 1} First line of verse
  {c:Chorus} First line of chorus
  {c:Verse 2} First line of second verse
  {c:Chorus} First line of chorus
  {c:Outro}
  ```

## Header
- **Title**: Include the song title using the `{t: <Song Title>}` directive.
- **Subtitle/Artist**: Include the artist or band name using the `{st: <Artist Name>}` directive.
- **Key**: Specify the song's key using the `{key: <Key>}` directive (e.g., `C`, `Am`, `F#m`).
- **Metronome**: Include the tempo in beats per minute (BPM) using the `{metronome: <xxx>}` directive. Source the tempo from reliable references like SongBPM, Musicstax, or Tunebat, if available.
- **Duration**: Include the song duration in minutes and seconds using the `{duration: <M:SS>}` directive. Source the duration from reliable references like Apple Music or Musicstax for the album version.
- **Example**:
  ```
  {t: Song Title}
  {st: Artist Name}
  {key: C}
  {metronome: 120}
  {duration: 3:45}
  ```

## Sections
- **Section Markers**:
  - Use `{sop: <Section Name>}` (start of part) and `{eop}` (end of part) for non-chorus sections (e.g., Intro, Verse, Pre-Verse, Bridge, Solo, Interlude, Outro, Main Theme, Fade Out).
  - Use `{soc}` (start of chorus) and `{eoc}` (end of chorus) for Chorus sections.
- **Section Naming**:
  - Label sections exactly as provided in the input (e.g., `Intro`, `Verse 1`, `Pre-Chorus`, `Bridge`, `Solo`, `Outro`).
  - For multiple instances of the same section type, label sequentially (e.g., `Bridge 1`, `Bridge 2`, `Solo 1`, `Solo 2`).
  - Preserve unique section names like `Main Theme` or `Pre-Verse` as provided.

## Chords
- **Placement**: Place chords in `[brackets]` above the lyrics, aligned with the corresponding words or phrases where chord changes occur.
- **Omission of Duplicates**: Omit duplicate chords within the same section if the progression remains unchanged (e.g., if `[C]` is followed by more lyrics in the same section without a chord change, do not repeat `[C]` until a new chord appears).
- **Chord Interpretation**: Interpret chords as per standard notation (e.g., `C` as major, `Cm` as minor, `C7` as dominant 7th, `Cmaj7` as major 7th, `C/E` as slash chord with E bass, `Csus4` as suspended 4th).
- **Alignment**: Ensure chords are placed directly above the word or syllable where the chord change occurs for clarity.

## Lyrics
- **Line Length**: Keep lyrics in longer lines, combining phrases where appropriate to reflect the natural flow of the song (e.g., "Just a small town girl livin' in a lonely world" as a single line), unless explicitly instructed to preserve original line breaks.
- **Preserve Stylistic Elements**: Retain stylistic elements, typos, or unique phrasing exactly as provided (e.g., "oooon", "al__ways", "ya'll", "four whell").
- **Punctuation and Spacing**: Preserve all punctuation, spacing, and capitalization as provided in the input.

## Specific Section Formatting
- **Intro**:
  - Label as `{sop: Intro}/{eop}`.
  - Include chords only, with `- - -` for instrumental sections without lyrics, avoiding `|`.
- **Verses**:
  - Label as `{sop: Verse <Number>}/{eop}` (e.g., `Verse 1`, `Verse 2`).
  - Place chords above lyrics, aligning with changes.
- **Pre-Verse/Pre-Chorus**:
  - Label as `{sop: Pre-Verse}/{eop}` or `{sop: Pre-Chorus}/{eop}` as provided.
  - Include chords and any associated lyrics.
- **Chorus**:
  - Label as `{soc}/{eoc}`.
  - Include chords and lyrics, preserving repetition and stylistic breaks (e.g., underscores in "al__ways").
- **Bridge**:
  - Label as `{sop: Bridge}/{eop}` or `{sop: Bridge <Number>}/{eop}` for multiple bridges.
  - Include chords and any lyrical content.
- **Solo**:
  - Label as `{sop: Solo}/{eop}` or `{sop: Solo <Number>}/{eop}` for multiple solos.
  - Include chords, with `- - -` for instrumental measures without lyrics, avoiding `|`.
- **Interlude**:
  - Label as `{sop: Interlude}/{eop}`.
  - Include chords and any lyrical or spoken content.
- **Outro/Fade Out**:
  - Label as `{sop: Outro}/{eop}` and `{sop: Fade Out}/{eop}` if a fade-out is specified.
  - Include chords and lyrics, preserving fade-out indication