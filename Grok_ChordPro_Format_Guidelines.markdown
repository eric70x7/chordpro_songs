# ChordPro Format Guidelines

These guidelines outline the preferred ChordPro format for structuring and presenting song chord sheets, based on specific formatting preferences. The format is designed to be clear, consistent, and compatible with standard ChordPro conventions, with additional details for tempo, duration, and section handling.

## Header
- **Title**: Include the song title using the `{t: <Song Title>}` directive.
- **Subtitle/Artist**: Include the artist or band name using the `{st: <Artist Name>}` directive.
- **Key**: Specify the song's key using the `{key: <Key>}` directive (e.g., `C`, `Am`, `F#m`).
- **Tempo**: Include the tempo in beats per minute (BPM) using the `{tempo: <Value> BPM}` directive. Source the tempo from reliable references like SongBPM or Musicstax, if available.
- **Duration**: Include the song duration in minutes and seconds using the `{duration: <M:SS>}` directive. Source the duration from reliable references like Apple Music or Musicstax for the album version.
- **Example**:
  ```
  {t: Song Title}
  {st: Artist Name}
  {key: C}
  {tempo: 120 BPM}
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
- **Line Length**: Keep lyrics in longer lines, combining phrases where appropriate to reflect the natural flow of the song (e.g., "Just a small town girl livin' in a lonely world" as a single line).
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
  - Include chords and lyrics, preserving fade-out indication if provided.
- **Main Theme**:
  - Label as `{sop: Main Theme}/{eop}` for recurring instrumental or thematic sections.
  - Include chords only, unless lyrics are provided.

## General Formatting
- **Content Type**: Use `text/plain` for ChordPro files.
- **Artifact ID**: Assign a unique UUID for each new song (e.g., `4b9d2e7c-5f8a-4e6b-a3f9-2j0f4h1c3g6j`). Use the same artifact ID for updates to a previous song, if applicable.
- **File Naming**: Use the song title followed by the artist in the title attribute (e.g., `title="Song Title - Artist Name"`).
- **No Nesting**: Do not nest `<xaiArtifact>` tags or mention them outside the tag content.
- **Preserve Source**: Maintain all lyrics, chords, and section labels exactly as provided, including any errors or stylistic choices, unless explicitly instructed to correct.

## Example
Below is an example of a formatted song in the preferred ChordPro format:

```
{t: Sample Song}
{st: Sample Artist}
{key: G}
{tempo: 120 BPM}
{duration: 3:30}

{sop: Intro}
[G] [C] [D]
- - -
{eop}

{sop: Verse 1}
[G]       [C]
I walk down the road alone
[D]
Trying to find my way
[G]       [C]
With a heart that's made of stone
[D]
I face another day
{eop}

{soc}
[G]
This is the chorus line
[C]       [D]
Singing loud and clear
[G]
Never gonna give up trying
[C]       [D]
I'll be forever here
{eoc}

{sop: Solo}
[G] [C] [D]
- - -
{eop}

{sop: Outro}
[G]       [C]
Keep on moving forward
[D]
Till the end of time
{eop}
```

## Notes
- Always source tempo and duration from reliable references (e.g., SongBPM, Musicstax, Apple Music) for accuracy.
- If no tempo or duration is available, note this in the response outside the artifact, but still include the `{tempo:}` and `{duration:}` directives with placeholders or estimates, if instructed.
- For instrumental sections like solos or intros, use `- - -` to indicate measures without lyrics, ensuring no use of `|`.
- Ensure chord alignment enhances readability, especially for longer lyric lines or complex progressions.
- If updating a previous song, preserve the original artifact ID and update only the specified sections, keeping unchanged content intact.

These guidelines ensure a consistent and professional ChordPro format tailored to your preferences, suitable for both performance and archival purposes.