# Slide grammar

Every deck is built from these ten slide types and nothing else. An audience
profile is a *sequence* of these types with a length cap; the content comes
from the source artifact. Each type below shows its job, its rules, and the
Marp markup that produces it with the `operator` theme.

This file owns every slide-level rule — placement, bullets, headlines,
numbers, caveats. Profiles own only sequence, cap, tone, and strip/add. If a
profile seems to disagree with this file, this file wins.

## Two kinds of headline

**Claim headlines** — `answer`, `point`, `evidence`, `options`, `ask` — are full
sentences that assert something and can be true or false. Read in order they
are the deck's argument; the headline test reads these and only these.

**Label headlines** — `title`, `agenda`, `section`, `next`, `appendix` — name a
thing. They are exempt from the headline test.

## Rules for any number on any slide

1. **It traces to the source artifact.** No number, count, or comparison the
   source does not contain. Compressing two source facts into a new claim
   ("three independent samples show…") is fabrication, even when each fact
   is real.
2. **It carries the source's confidence.** A claim the source tags `inferred`
   or lists as contested gets a hedge verb or a one-line caveat — never a
   flat statement. A claim the source tags `observed` may be stated flat.
3. **It carries a date when staleness matters.** If the figure is more than
   about a year old, or the audience would assume it is current, the slide
   says when it's from.
4. **It carries its boundary when the boundary changes the meaning.** "88%
   contribute" and "88% fund their own wedding" are different claims.
5. **An absence is a claim too.** "No one has measured X" is only sayable if
   the source records looking and not finding (tagged `unknown` or listed as
   a gap). Otherwise say what's defensible: "this research found no
   measurement of X."

Plan parameters — headcount, weeks, dates, conversation counts on `ask` and
`next` slides — are commitments, not findings, and are exempt from rule 1.

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
**Rules:** one line of purpose that names the decision or action the deck is
for; no agenda here.

```markdown
<!-- _class: title -->
# [Deck name]

[One line: what this deck is for.]

[Date] · [Presenter or team] · For: [audience]
```

## `answer`

**Job:** the conclusion, up front, before any evidence.
**Rules:** the headline is the answer as a full sentence. Two to four lines
of support, in order of strength — every `point` slide that follows must be
one of them; a point the answer didn't set up is a surprise. If the reader
stops here, they have the point.

A caveat that governs the whole deck — a sample bias, a boundary, a
definition every number depends on — goes here, as the last line. It is the
one place a deck-wide caveat lives.

```markdown
<!-- _class: answer -->
# [The conclusion as a complete sentence.]

- [The strongest reason]
- [The next]
- [The next]

*[Deck-wide caveat, one line, if there is one.]*
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
in the first 30 days," not "Churn analysis"). Body is **at most three bullets,
or one visual** — never both, never two ideas. A headline joined by "and" is
usually two ideas.

The first bullet carries the headline's number with enough source to defend
it (name and date). The other bullets are mechanism or consequence — why it's
true, what it changes — not more numbers. If the point needs a table to
hold, the table is an `evidence` slide directly behind it.

```markdown
# [A sentence that claims something.]

- [Support]
- [Support]
- [Support]
```

## `evidence`

**Job:** the data behind a point — a table, a chart, or sourced numbers.
**Rules:** the headline is a claim, not a label — "Accounts that connect data
in week one retain at 91%," not "Retention by cohort" — and it claims only
what the rows beneath it show. Every number has a source and a date on the
slide; boundaries stated for any market or usage figure.

**Placement:** an `evidence` slide sits directly behind the `point` it
supports. Never free-standing, never in a slot of its own. It belongs in the
main deck only when the number is **load-bearing** — the point's headline is
false without it. Otherwise it goes to the appendix. Profiles say how many
the audience tolerates in the main deck; this rule says where they go.

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
**Rules:** one ask. Named decider. Date. What saying yes commits. What happens
if it isn't made. The ask must be something the preceding slides argued for
— an ask that introduces new reasons on the ask slide has skipped a point.

The decider is a person; a role is acceptable when the person isn't yet
assigned ("VP Product," "the steering-group chair"). "Leadership" or "the
team" is not a decider. If the deck is informational, the ask slide says so
in one line rather than being omitted.

```markdown
<!-- _class: ask -->
# We're asking for [the decision].

**Decider:** [who] · **By:** [date]
**Scope:** [what yes commits — people, weeks, money, one line]
**If not decided:** [consequence]
```

## `next`

**Job:** what happens after this meeting.
**Rules:** owners and dates, three to five lines. An owner is a person or a
role, same standard as the decider — a team name is not an owner. Effort
and elapsed time are stated separately when they differ ("four weeks of one
person over seven calendar weeks").

```markdown
# What happens next
| Step | Owner | When |
|---|---|---|
```

## `appendix`

**Job:** everything that would derail the main flow — methodology, full data,
caveats, the long version.
**Rules:** after a divider. Unlimited in count. Nothing in the appendix is
required to follow the main deck. The number rules above still apply; the
one-idea and bullets-or-visual rules do not — an appendix slide may carry a
table with notes beneath it.

```markdown
<!-- _class: section -->
# Appendix

---

<!-- _class: appendix -->
# [Appendix slide title]
…
```
