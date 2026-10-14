# Field language and clear exposition

Use this guide when drafting or revising prose that reads stiffly, hides simple
actions behind abstract nouns, mixes inconsistent terminology, or forces the
reader to reconstruct missing steps. All examples below are synthetic; apply
their underlying principles to the manuscript's actual content.

## Choose words by their job

Cryptographic prose relies on two kinds of vocabulary working together: **exact
technical nouns** and **plain action verbs**.

- **Lock technical nouns to their definitions.** Use the term established in the
  relevant subfield (`commitment`, `witness`, `random oracle`, `evaluation key`,
  `simulator`, `advantage`). Once you name a formal object, keep that exact name
  throughout the paper. Never substitute synonyms ("evidence" for "witness",
  "verifier check value" for "commitment", "scheme" vs. "protocol" vs. "primitive"
  interchangeably) just for stylistic variety—in mathematical writing, a new word
  signals a new object.
- **Use direct verbs for ordinary operations.** Prefer concrete verbs that state
  what happens in the protocol or proof: `computes`, `samples`, `sends`, `checks`,
  `accepts`, `aborts`, `bounds`, `reduces`, `interpolates`, `amortizes`. Use a
  specialized verb only when it captures a real technical distinction.
- **Define genuinely new terms once, at the point of need.** Do not coin compound
  buzzwords or metaphorical labels when standard terminology or a plain description
  works. If a new concept needs a name, state what it is before using the label.

When a terminology choice recurs across sections, note the chosen term and its
distinction from nearby terms in `STATE.md` or existing notation notes so later
sections stay consistent.

## Cut empty framing and nominalizations

Watch for five high-frequency habits that bloat academic drafts and obscure
the technical message:

- **Unbacked praise and marketing adjectives:** Words like *novel, powerful,
  seamless, remarkable, significant, ultra-fast* add no information on their own
  and invite reviewer skepticism. Replace the adjective with the specific structural
  difference or measured quantity, or cut it.
- **Zombie nouns (nominalizations):** Turning verbs into abstract noun chains
  (*"performs the computation of"*, *"achieves the reduction of"*, *"provides the
  capability for verification"*) hides who acts and what changes. Name the actor
  (the prover, the simulator, Algorithm 2) and restore the active verb.
- **Vague glue verbs:** Verbs like *leverage, utilize, facilitate, attain,
  retain* often blur the mechanism. Instead of writing that a construction
  *"retains public verifiability"* or *"leverages commitments to facilitate
  checking"*, state the exact guarantee or action: *"allows any party to verify
  the proof from the public transcript"* or *"uses the commitment to check..."*.
  Reserve *"retain"* for when an algorithm literally keeps an object in memory or
  leaves an inherited step untouched.
- **Throat-clearing and meta-narration:** Cut openings that merely announce an
  intention to write (*"In this paragraph, we will explain how..."*, *"It is
  important to note that..."*, *"Before proceeding, we first point out..."*). Lead
  directly with the technical claim, question, or step. Keep signposts only when
  they orient the reader across a genuine structural boundary.
- **Mechanical sentence templates:** Starting every paragraph with *"First, ...
  Second, ..."* or *"Furthermore, ... Moreover, ..."* substitutes conjunctive
  stickers for logical flow. Let the connection between ideas carry the transition.

Treat words like `robust`, `extract`, `efficient`, or `sound` according to their
context: when they refer to formal properties (robust secret sharing, witness
extraction, polynomial-time efficiency), keep them exact; when used as vague
praise, replace them with the concrete property.

## Control sentence flow and math-in-prose grammar

### Lead with the familiar, end with the new (Given-before-New)

Readers follow complex technical arguments most easily when each sentence starts
with **familiar context** (an object just introduced, a shared assumption, or the
step just completed) and ends with the **new information** (the key obstacle,
the complexity bound, or the newly introduced mechanism).

- If a sentence feels tangled, check whether the new, heavy technical payload is
  crammed into a long grammatical subject before the main verb. Move familiar
  links to the front and push the new insight or formula to the end where
  reader emphasis naturally lands.
- Resolve naked pronouns (`this`, `that`, `it`, `which`) at the start of a
  sentence by pairing them with an explicit noun: `this reduction`, `this degree
  bound`, `this round-trip cost`.

### Integrate symbols and equations into English grammar

Mathematical expressions are parts of speech within the sentence, not detached
illustrations:

- **Never start a sentence with a bare symbol or number.** Write `"The polynomial
  $f(X)$ has degree at most $d$."` rather than `"$f(X)$ has degree at most $d$."`
- **Pair new symbols with a category noun on first use.** Writing `"Let $d$ be
  the ring dimension and $\mathbf{c} \in \mathbb{Z}_q^n$ the challenge vector"`
  is much easier to parse and remember than `"Let $d$ and $\mathbf{c} \in
  \mathbb{Z}_q^n$ be given."`
- **Keep displayed equations grammatically connected.** Introduce a displayed
  equation with a complete clause ending in a colon, or weave it directly into
  the sentence as the object of a verb (`"...satisfies [equation], where..."`),
  with proper end punctuation. Explain what a formula means or why it holds—do
  not drop a wall of notation without stating the relationship it captures.
- **Avoid adjacent unseparated math tokens.** Write `"for each $i \in [n]$, the
  party holds $x_i$"` rather than `"for $i \in [n]$ $x_i$ is held"`.

### Keep conditions attached to the claims they limit

Do not shorten a sentence by stripping its security model, asymptotic regime,
or parameter constraint. When splitting a long multi-clause sentence for
readability, keep the qualifying condition (`under the DDH assumption`, `when the
public index is fixed`, `for ring dimension $N \ge 2^{14}$`) in the same sentence
as the claim it governs.

## Synthetic revisions

### Replace nominalizations and glue verbs with direct actions

- **Original:** "The verifier leverages the commitment to facilitate the
  validation of the prover's response."
- **Revision:** "The verifier uses the commitment to check the prover's response."
- **Why:** Restores the concrete verb (`uses ... to check`) without inventing
  new protocol claims. If the protocol specifies the exact check (e.g., opening
  at a random challenge point $z$), name that check directly.

### Align sentence flow from familiar context to new insight

- **Original:** "The necessity of recomputing the public lookup table from the
  parameters $K$ on every query even when $K$ is unchanged across a batch causes
  the baseline verifier's setup bottleneck."
- **Revision:** "In the baseline verifier, each query rebuilds the public lookup
  table from the parameters $K$. Because this table depends only on $K$, queries
  sharing the same parameters repeat identical setup work."
- **Why:** The original buries the main verb at the very end of a 24-word abstract
  subject. The revision starts with the familiar setting, states the concrete
  operation, and lands on the key observation (repeated identical setup).

### Unpack dense clauses while preserving exact conditions

- **Original:** "When the public index remains unchanged, its reuse across
  requests eliminates repeated index construction while preserving the
  per-request checks."
- **Alternative for a dense surrounding passage:** "When the public index remains
  unchanged, requests can reuse it instead of rebuilding it each time. Each
  request still runs the full verification check."
- **Why:** Either version is accurate; the split version lowers cognitive load
  when adjacent sentences are already heavy with notation, while keeping the
  condition (`When the public index remains unchanged`) attached to reuse.

### Keep formal terminology intact while explaining its role

- **Draft with synonym drift:** "The prover holds a witness $w$ for $x$. To hide
  this secret evidence, the prover commits to the credential before receiving the
  challenge."
- **Revision:** "The prover holds a witness $w$ satisfying $R(x, w) = 1$. To hide
  $w$, the prover commits to it before receiving the verifier's challenge."
- **Why:** Calling the same object `witness`, `secret evidence`, and `credential`
  in two sentences forces the reader to check whether three distinct objects exist.

## Final check before delivering prose

Scan the draft for the five friction points that most often slow down a
cryptography reviewer:
1. Undefined or drifting names for the same formal object.
2. Abstract noun chains or passive constructions that hide which party performs
   an operation.
3. Naked `this`/`it` openings or bare symbols starting a sentence.
4. Claims separated from their assumptions, quantifiers, or parameter bounds.
5. Unexplained leaps between two consecutive equations or protocol steps.

Verify that all notation, citation keys, numerical values, and claim scopes
match the source material before returning the text.
