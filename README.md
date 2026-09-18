# Chef OS

Danielius's canonical, version-controlled cookbook and cooking learning system.

Start with [the manifest](knowledge/00-Chef-OS-Manifest.md). It defines authority, read order, file ownership, and the persistence contract. [Chef Rules](knowledge/03-Chef-Rules.md) owns cooking and recipe-update behavior.

## Navigation

- [Chef Profile](knowledge/01-Chef-Profile.md): stable preferences and constraints.
- [Kitchen and Equipment](knowledge/02-Kitchen-and-Equipment.md): known kitchen capabilities.
- [Chef Rules](knowledge/03-Chef-Rules.md): operating, adaptation, experiment, and safety policy.
- [Ingredient Defaults](knowledge/04-Ingredient-Defaults.md): units and ingredient conventions.
- [Recipe Registry](knowledge/05-Recipe-Registry.md): canonical recipe index and capture queue.
- [Recipe template](templates/recipe-template.md): required recipe structure.
- [Experiment template](templates/experiment-template.md): material test structure.
- [Project entry point](PROJECT-INSTRUCTIONS.md): compact text for ChatGPT Project instructions.
- [Changelog](CHANGELOG.md): architecture history and verification record.

## Validation

Run:

```bash
python3 scripts/validate_os.py
```

The validator uses only Python's standard library. It checks required owners, recipe metadata, identifiers, recipe sections, internal links, and common version-debris patterns. It does not judge taste, food safety, or whether a recipe will succeed.

Then review [the behavioral scenarios](tests/chef-scenarios.md) and inspect the complete diff before publishing architecture or policy changes.

## Integration boundary

GitHub is the canonical mutable store. ChatGPT is the conversational interface. Current conversation supplies immediate context such as available ingredients, servings, timing, desired result, and cooking feedback.

Adapting a recipe for one meal does not change the canonical recipe. A canonical update requires an explicit save/update instruction or acceptance of a clearly proposed change.

## Maintenance scope

Keep one owner per responsibility. Update canonical recipes in place. Git history preserves earlier versions, so do not create files such as `kugelis-v2-final.md`. Store an experiment only when it tests a material uncertainty or produces durable learning.
