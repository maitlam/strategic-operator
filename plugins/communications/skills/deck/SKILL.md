---
name: deck
description: >
  Build a slide deck from an existing analysis — a brief, a status report, a
  portfolio read, a roadmap — using a fixed slide grammar and an audience
  profile, and render it from markdown with Marp. Use whenever the user needs
  slides, a presentation, a readout, a deck for a meeting, or asks to "turn
  this into slides," "make a deck," "present this to leadership," or "what
  would this look like for the board / the team / a partner." Not for the
  analysis itself; that comes from another skill and this one shapes it for a
  room.
license: MIT
metadata:
  provenance: original
  author: maitlam
  version: 0.1.0
---

# Deck

An analysis and an audience in. A deck that makes one argument to that room, rendered and ready, out.

## The framework behind this

A deck is an argument, not a document with page breaks. The failure mode is the document deck: every slide a topic heading, every body a paragraph, the point somewhere around slide fourteen if the reader is still there. It happens because the deck was built by pouring content in and cutting, rather than by deciding what the room needs to conclude and building only that.

Three disciplines.

**Every slide headline is a sentence that claims something.** "Q3 pipeline" is a label. "Q3 pipeline is 40% short of the number we committed to" is a claim — it can be true or false, it tells the reader what the slide is for, and read in sequence the headlines are the whole argument. The test of a finished deck is whether the headlines alone, read down the left of the outline, make the case. If they don't, the deck isn't finished.

**One idea per slide, and the evidence lives next to it or in the appendix — never on it.** A slide carrying a claim, three bullets, and a chart is asking the reader to do the synthesis the author skipped. The `point` slide makes the claim; the `evidence` slide behind it holds the numbers with their sources; the appendix holds everything the room might ask for and shouldn't have to sit through.

**The audience decides the sequence, not the content.** The same research brief becomes a ten-slide answer-first deck for executives, a twenty-five-slide show-the-work deck for the team, and a twelve-slide what's-in-it-for-you deck for a partner. The evidence is shared; what changes is the order, the length, what's stripped, and what's added. That's what the audience profiles in `references/` encode — a sequence of slide types, a cap, tone rules, and a strip-and-add list. Building for an audience means following the profile, not guessing at the tone.

The deck is built from a fixed grammar — ten slide types, defined in `references/slide-grammar.md` — so profiles can be precise and decks can be compared. A slide that doesn't fit one of the ten types is usually two slides or none.

## Gather first

Ask for what's missing; don't assume.

- **The source.** The artifact this deck presents — a brief, a report, a roadmap, an analysis from another skill. If the user has only an idea and no artifact, point them at the skill that produces one first. This skill shapes; it doesn't analyze.
- **The audience.** `exec`, `internal`, `external`, or `board`. If it's unclear, the question "who has to do something after seeing this?" usually settles it.
- **The occasion.** How long is the slot, is it presented or sent, is there a decision on the table.
- **The ask.** What should the room decide or do. If there's genuinely none, the deck is informational and the profile will shorten it.

## Process

1. **Read the source fully** and write the answer in one sentence. That sentence becomes the `answer` slide's headline and the deck's spine. If it can't be written, the source isn't ready to present.
2. **Load the audience profile** from `references/audience-<name>.md`. Take its sequence, cap, tone rules, and strip/add list as constraints, not suggestions.
3. **Outline in headlines.** For each slot in the profile's sequence, write the slide's headline as a claiming sentence. Read the claim headlines (`answer`, `point`, `evidence`, `options`, `ask`) top to bottom — label types are exempt. Every `point` headline must already appear, in short form, on the `answer` slide. Fix the argument here, before any body content exists — it's ten times cheaper.
4. **Fill the bodies** from the source. `point` slides get three bullets or one visual. `evidence` slides get the numbers with sources and boundaries. Strip what the profile says to strip; add what it says to add.
5. **Write the `ask`** — named decider, date, scope of what yes commits, consequence of no decision. The ask must follow from the points: if it asks for something no preceding slide argued for, add the point or change the ask. If the profile calls for one and the source has none, ask the user; don't invent an ask. If the ask is to close gaps, the method must be one the source says can close them.
6. **Move everything else to the appendix.** If the main deck exceeds the cap, the argument has too many points; cut points, don't shrink type.
7. **Write `deck.md`** with the frontmatter contract and the grammar markup, then **render** with `scripts/render.sh deck.md --pdf` (add `--html` or `--pptx` as needed).
8. **Run the headline test** on the rendered deck: claim headlines only, top to bottom. Then the **cover test**: hide every slide except `answer` and `ask` — can the room decide? If either fails, go back to step 3.

## Output

Two files, plus a short handoff.

**`<name>-<audience>.md`** — Marp source. Frontmatter sets `marp: true`, `theme: operator-<audience>`, `paginate: true`, and header/footer naming the deck, audience, date, and source artifact. Slides follow the grammar in `references/slide-grammar.md`.

**`<name>-<audience>.pdf`** (and `.html` / `.pptx` on request) — rendered by `scripts/render.sh`.

**Handoff:** the answer sentence, the slide count against the cap, the ask, and anything the profile said to strip that the user may want to know was removed.

## Quality bar

- **The headlines alone make the argument.** This is the test; the rest is craft.
- **Under the profile's cap** without shrinking type or cramming. Over the cap means too many points, not too little room.
- **No slide with both bullets and a visual.** Pick.
- **Every number on an `evidence` slide has a source, a date, and a boundary.**
- **The `ask` names a decider, a date, and a scope**, or the deck says explicitly that it isn't asking for one.
- **Every number traces to the source at the source's confidence.** Nothing the source doesn't contain; nothing tagged `inferred` stated flat; nothing two source facts were compressed into. This is where fluent authors fail — the deck reads well and says something the source never said.
- **Nothing from the strip list survives into the main deck.** It goes to the appendix or goes away.
- **The deck can be sent without being presented.** If it only works with a voiceover, the headlines aren't doing their job.

## Engine

Marp, via `scripts/render.sh` and the themes in `assets/` — `operator` is the base; `operator-exec`, `operator-internal`, `operator-external`, and `operator-board` import it and adjust type size, density, and footer. The content contract — frontmatter fields, `---` separators, `<!-- _class: type -->` slide types — is deliberately plain so another renderer can be added behind the same source. Marp's PPTX export is image-based; treat it as a sendable artifact, not an editable one.
