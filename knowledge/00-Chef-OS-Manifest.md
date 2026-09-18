# Chef OS Manifest

Last updated: 2026-09-18
System version: 1.1
Canonical repository: `DanieliusIsiunas/cookbook`

## Authority and ownership

The default GitHub branch is the canonical mutable cooking store. Current explicit user instructions govern the present interaction. Old conversations, attachments, local files, and generated artifacts are historical evidence only when GitHub is available.

Each responsibility has one owner:

| Path | Responsibility |
|---|---|
| `knowledge/00-Chef-OS-Manifest.md` | Authority, read/write contract, ownership, and integration boundary |
| `knowledge/01-Chef-Profile.md` | Stable preferences and cooking constraints |
| `knowledge/02-Kitchen-and-Equipment.md` | Known equipment and kitchen capabilities |
| `knowledge/03-Chef-Rules.md` | Cooking, adaptation, experiment, safety, and persistence policy |
| `knowledge/04-Ingredient-Defaults.md` | Unit, naming, and ingredient conventions |
| `knowledge/05-Recipe-Registry.md` | Canonical recipe index, status, aliases, and capture queue |
| `recipes/` | One canonical file per recipe |
| `experiments/` | Material recipe experiments and durable findings, not canonical instructions |
| `templates/recipe-template.md` | Recipe structure, not recipe policy |
| `templates/experiment-template.md` | Experiment structure, not recipe policy |
| `PROJECT-INSTRUCTIONS.md` | Thin ChatGPT Project entry point |
| `scripts/validate_os.py` | Deterministic structural checks, not a culinary decision engine |
| `tests/chef-scenarios.md` | Behavioral evaluation cases, not recipes |
| `CHANGELOG.md` | Architecture and validation history |

System version is declared only here. Entry points and templates must not become alternative policy owners.

## Task-specific read order

### Retrieve or adapt a known recipe

1. Read this manifest.
2. Read `knowledge/01-Chef-Profile.md` and `knowledge/03-Chef-Rules.md`.
3. Read `knowledge/04-Ingredient-Defaults.md` when units, substitutions, or ingredient naming matter.
4. Read `knowledge/05-Recipe-Registry.md` to resolve title or alias.
5. Read the canonical recipe.
6. Use current conversation context for servings, ingredients on hand, time, desired outcome, and feedback.

### Review a completed cook or design an experiment

Follow the retrieval order, then read the relevant experiment file if one exists. Separate observation, causal hypotheses, alternatives, and proposed change.

### Change the operating system

Read every file under `knowledge/`, relevant templates, validation code, behavioral scenarios, and `CHANGELOG.md`. Validate the complete change and inspect the diff.

If required canonical content is unavailable, name the missing source. Do not present remembered or reconstructed content as the user's canonical recipe. Continue with clearly labeled general guidance when useful.

## Source-of-truth precedence

For conflicts:

1. Current explicit user statement for the present interaction.
2. Current canonical recipe for established recipe content.
3. Chef Rules for operating behavior.
4. Recipe Registry for identity, path, aliases, and lifecycle status.
5. Chef Profile and Kitchen and Equipment for stable personal context.
6. Accepted findings in a relevant experiment.
7. Historical conversations, attachments, and old generated content.

A one-off substitution, scale change, time constraint, or missing ingredient affects the current cook only unless Danielius explicitly saves it. An experiment does not override a recipe until its learning is adopted into the canonical recipe.

## Cooking and learning loop

Retrieve -> define the intended result -> identify current constraints -> adapt or isolate one useful variable -> cook using observable checkpoints -> capture outcome -> distinguish evidence from hypothesis -> propose the smallest durable change -> update only after authorization.

## Persistence and cleanup

- Persist a recipe change when Danielius directly asks to save/update it or accepts a clearly stated proposed change. Do not ask again when that authorization is already explicit.
- Fetch the current target and blob SHA before updating. Make the smallest coherent edit, reconcile intervening changes, and verify saved content.
- Update the same canonical path. Never create `v2`, dated, backup, copy, or `final` variants as version history.
- Use descriptive commit messages as the audit trail. Add architecture changes to `CHANGELOG.md`.
- Store durable recipe knowledge: quantities, method, equipment dependencies, sensory checkpoints, critical variables, validated variations, troubleshooting, and relevant provenance.
- Do not store ordinary chat, temporary pantry state, shopping lists, or every cook. Store an experiment only when it tests an important uncertainty or produces durable learning.
- Preserve uncertainty. Missing quantities, conflicting recollections, and untested conversions must remain explicit rather than being filled with plausible guesses.
- When a recipe becomes meaningfully different in intended result or technique, create a separate recipe with a clear relationship. Mere scaling or substitution is not a new recipe.

## Integration and validation contract

ChatGPT Project instructions route to this manifest and do not duplicate detailed policy. GitHub remains authoritative over Project Sources or copied files.

For architecture or schema changes:

1. Run `python3 scripts/validate_os.py`.
2. Evaluate `tests/chef-scenarios.md`.
3. Inspect the complete diff for lost constraints, invented recipe facts, duplicated owners, and competing rules.
4. Verify remote read-back before claiming success.

Structural validation cannot establish taste, correct technique, food safety, or recipe reliability. Those require cooking evidence and judgment.
