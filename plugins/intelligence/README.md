# intelligence

What a team knows about its market, and how it keeps knowing. Nine skills, three agents.

## The domain view

Market work fails in two directions. It goes shallow — a logo slide, a list of everyone in a space, no judgment. Or it goes deep on one company for a week and answers a question nobody asked.

The corrective is sequencing. **Segment the ecosystem before profiling anyone in it**, because a company only makes sense relative to the structure it sits in. Then profile against a fixed shape, so six profiles are comparable rather than six essays.

That handles the snapshot. The harder problem is making intelligence a *standing* function rather than a one-time exercise — and that's a loop, not a deliverable:

```
signal-scan  →  research-agenda  →  research-brief  →  pattern-analysis  →  intelligence-brief
  catch what       decide what         answer it          connect it            circulate what
  keeps coming     to answer, and                         across everything     matters
  up               why                                    heard
```

Each stage has a memory the next one reads: a signal log, a research roadmap, a set of briefs, a hypothesis ledger. The loop runs because the artifacts persist, not because anyone remembers to run it.

Three disciplines everything here shares. **Observation and inference stay visibly separate** — this material circulates and loses its caveats, and an unlabeled inference gets repeated as fact in a room where nobody can check it. **Independent sources are counted, not felt** — one person saying it three times is one source, and a theme is a claim about frequency. And **the output ends in questions, not conclusions**; desk research supports a discovery list, not a verdict.

Most of what this domain produces is negative information — segments and targets that turned out not to matter, questions the public record can't answer. That's the function working, and it's worth saying out loud so the effort isn't judged on how many partners it produced.

| Skill | In → Out |
|---|---|
| `ecosystem-map` | An unfamiliar market → its structure, and who to go talk to |
| `market-sizing` | A market and a boundary → a defensible range and the assumption that drives it |
| `signal-scan` | Recent internal notes → a signal log that remembers what keeps coming up |
| `research-agenda` | Open questions → a ranked roadmap, each tied to a decision |
| `research-brief` | One topic → a sourced brief, and what it couldn't settle |
| `pattern-analysis` | The whole corpus → what recurs, what conflicts, how the hypotheses stand |
| `intelligence-brief` | Raw signals → five items with a "so what" attached |
| `partner-scan` | A named company → a profile ending in what would have to be true |
| `competitive-intel` | A competitor → their strategy and structural exposure |

## Install

```
/plugin marketplace add maitlam/strategic-operator
/plugin install intelligence@strategic-operator
```

## Skills

<!-- catalog:start -->
| Skill | Type | What it does |
|---|---|---|
| [`competitive-intel`](skills/competitive-intel/SKILL.md) | Original | Build a read on a competitor — what they're actually doing versus what they say, where they're strong, where they're exposed, and what their recent moves imply about… |
| [`ecosystem-map`](skills/ecosystem-map/SKILL.md) | Original | Segment an unfamiliar market or ecosystem into its structural parts — who the actors are, how value and money move between them, and where the pain concentrates |
| [`intelligence-brief`](skills/intelligence-brief/SKILL.md) | Original | Produce a recurring market intelligence brief — daily or weekly signals filtered for what actually matters to this team, with the "so what" attached |
| [`market-sizing`](skills/market-sizing/SKILL.md) | Original | Size a market with a defensible range rather than a single number — TAM, SAM, and SOM built bottom-up and top-down, reconciled, with every assumption visible and the one… |
| [`partner-scan`](skills/partner-scan/SKILL.md) | Original | Profile a specific company as a potential partner — what they do, who they serve, how they make money, what they'd want from a partnership, and what would have to be… |
| [`pattern-analysis`](skills/pattern-analysis/SKILL.md) | Original | Read across a whole corpus of conversations — meeting notes, interviews, customer calls, briefs — and report what recurs, what conflicts, what is newly emerging, and how… |
| [`research-agenda`](skills/research-agenda/SKILL.md) | Original | Turn a pile of open questions, graduated signals, and untested assumptions into a prioritized research roadmap — each item framed by the decision it feeds and what… |
| [`research-brief`](skills/research-brief/SKILL.md) | Original | Produce a deep, sourced research brief on a single topic — scope confirmed first, the topic decomposed into lenses so coverage is systematic, every fact sourced and… |
| [`signal-scan`](skills/signal-scan/SKILL.md) | Original | Sweep the team's own recent conversations — meeting notes, customer calls, interviews, internal briefs — for research signals, deduplicate them against a running signal… |
| [`lens-researcher`](agents/lens-researcher.md) (agent) | Original | Research one lens of a larger topic — money, operations, players and moves, technology, evidence, or constraints — against a short list of sub-questions, writing sourced… |
| [`market-landscape-analyzer`](agents/market-landscape-analyzer.md) (agent) | Original | Map an unfamiliar market, space, vertical, or ecosystem — segment the actors, trace value and money flow, identify pain concentration, and flag white space |
| [`partner-intelligence`](agents/partner-intelligence.md) (agent) | Original | Research and profile a named company or organization as a potential partner, vendor, channel, or acquirer target |
<!-- catalog:end -->

## Hooks

Ships one hook. It's active for anyone who installs this plugin; silence it with an env var rather than uninstalling.

| Event | Script | What it does | Off switch |
|---|---|---|---|
| `PostToolUse` (Write / Edit) | [`note-signals.sh`](hooks/note-signals.sh) | When a markdown file lands in the notes directory, asks Claude to run `signal-scan` on just that file and show candidate signals — deduplicated against the log — **for your confirmation** before the signal log is updated. The hook itself extracts and writes nothing. | `SO_NOTE_SIGNALS=off` |

Paths, relative to the project root (override with env vars):

| Env var | Default | Meaning |
|---|---|---|
| `SO_NOTES_DIR` | `meetings/` | Where processed meeting notes land (shared with the bizops plugin) |
| `SO_SIGNAL_LOG` | `signal-log.md` | The signal log `signal-scan` maintains |

If bizops is also installed, a new note triggers both hooks: actions to the register, signals to the log. Each asks before writing.
