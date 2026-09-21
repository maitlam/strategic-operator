# Slide grammar

Every deck is built from these ten slide types and nothing else. An audience
profile is a *sequence* of these types with a length cap; the content comes
from the source artifact. Each type below shows its job, its rules, and the
Marp markup that produces it with the `operator` theme.

Slides are separated by `---`. A slide's type is set with `<!-- _class: type -->`
on its first line. The audience is chosen once, in frontmatter, by picking the
theme variant: `operator-exec`, `operator-internal`, `operator-external`, or `operator-board`.
(Marp's `_class` replaces rather than adds to a deck-level class, which is why
audience lives in the theme and slide type lives in the class.)

## Frontmatter (every deck)

```markdown
---
marp: true
theme: operator-exec   # operator-exec | operator-internal | operator-external | operator-board
paginate: true
header: "[Deck name] · [Audience]"
footer: "[Date] · [Source artifact]"
---
```

---

## `title`

**Job:** name the deck, the date, the audience, and its purpose in one line.
**Rules:** one line of purpose; no agenda here.

```markdown
<!-- _class: title -->
# [Deck name]

[One line: what this deck is for.]

[Date] · [Presenter or team] · For: [audience]
```

## `answer`

**Job:** the conclusion, up front, before any evidence.
**Rules:** the headline is the answer as a full sentence. Two to four lines
of support at most. If the reader stops here, they have the point.

```markdown
<!-- _class: answer -->
# [The conclusion as a complete sentence.]

[Two to four lines: the strongest reasons, in order.]
```

## `agenda`

**Job:** orient the reader in a long deck.
**Rules:** only when the deck has more than eight main slides. Section names,
not slide titles.

```markdown
# What's in this deck
1. [Section]
2. [Section]
3. [Section]
```

## `section`

**Job:** divider between parts.
**Rules:** a name and, optionally, the one thing the section establishes.

```markdown
<!-- _class: section -->
# [Section name]
[What this section establishes, one line.]
```

## `point`

**Job:** one idea.
**Rules:** the headline is a sentence that claims something ("Churn concentrates
in the first 30 days," not "Churn analysis"). Body is three bullets or one
visual. Never both. Never two ideas.

```markdown
# [A sentence that claims something.]

- [Support]
- [Support]
- [Support]
```

## `evidence`

**Job:** the data behind a point — a table, a chart, or sourced numbers.
**Rules:** every number has a source and a date on the slide. Boundaries stated
for any market or usage figure. Belongs immediately after the point it
supports, or in the appendix for exec decks.

```markdown
<!-- _class: evidence -->
# [What the data shows, as a sentence.]

| Metric | Value | Period |
|---|---|---|
| … | … | … |

<p class="source">Source: [name, date]. Boundary: [what's counted].</p>
```

## `options`

**Job:** choices with tradeoffs, when a decision is being asked for.
**Rules:** two to four options. Same columns for each. The recommended option
is marked, not buried.

```markdown
# [The choice, as a question.]

| | Option A | Option B (recommended) | Option C |
|---|---|---|---|
| What it is | | | |
| Cost | | | |
| Risk | | | |
| Reversible? | | | |
```

## `ask`

**Job:** the decision requested — by whom, by when — or, if no decision, what
the audience is being asked to do.
**Rules:** one ask. Named decider. Date. What happens if it isn't made.

```markdown
<!-- _class: ask -->
# We're asking for [the decision].

**Decider:** [who] · **By:** [date]
**If not decided:** [consequence]
```

## `next`

**Job:** what happens after this meeting.
**Rules:** owners and dates. Three to five lines.

```markdown
# What happens next
| Step | Owner | When |
|---|---|---|
```

## `appendix`

**Job:** everything that would derail the main flow — methodology, full data,
caveats, the long version.
**Rules:** after a divider. Unlimited. Nothing in the appendix is required to
follow the main deck.

```markdown
<!-- _class: section -->
# Appendix

---

<!-- _class: appendix -->
# [Appendix slide title]
…
```
