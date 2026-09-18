#!/usr/bin/env python3
"""Structural validator for Chef OS.

Uses only Python's standard library. This is not a food-safety or recipe-quality
validator.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "CHEF-OS.md",
    "PROJECT-INSTRUCTIONS.md",
    "CHANGELOG.md",
    "knowledge/00-Chef-OS-Manifest.md",
    "knowledge/01-Chef-Profile.md",
    "knowledge/02-Kitchen-and-Equipment.md",
    "knowledge/03-Chef-Rules.md",
    "knowledge/04-Ingredient-Defaults.md",
    "knowledge/05-Recipe-Registry.md",
    "templates/recipe-template.md",
    "templates/experiment-template.md",
    "experiments/README.md",
    "tests/chef-scenarios.md",
]

REQUIRED_METADATA = {
    "id",
    "title",
    "status",
    "servings",
    "prep_time_minutes",
    "cook_time_minutes",
    "total_time_minutes",
    "tags",
    "source",
    "updated",
    "schema_version",
}

REQUIRED_SECTIONS = [
    "Intended result",
    "Ingredients",
    "Equipment",
    "Method",
    "Sensory checkpoints",
    "Chef tips",
    "Critical variables",
    "Proven variations",
    "Troubleshooting",
    "Serving and storage",
    "Provenance",
]

ALLOWED_STATUSES = {"draft", "testing", "trusted"}

REQUIRED_CHEF_RULE_SNIPPETS = [
    "one or two high-leverage touches",
    "Preparation time and cooking time",
    "approximately 300 words",
    "Detail mode",
    "Flag common allergens",
]


def parse_front_matter(text: str, path: Path) -> dict[str, object]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: missing YAML-style front matter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{path}: unterminated front matter") from exc

    result: dict[str, object] = {}
    current_list: str | None = None
    for raw in lines[1:end]:
        if not raw.strip():
            continue
        if raw.startswith("  - ") and current_list:
            value = raw[4:].strip()
            assert isinstance(result[current_list], list)
            result[current_list].append(value)
            continue
        match = re.match(r"^([a-z_]+):\s*(.*)$", raw)
        if not match:
            raise ValueError(f"{path}: unsupported front-matter line: {raw}")
        key, value = match.groups()
        if value == "":
            result[key] = []
            current_list = key
        elif value == "[]":
            result[key] = []
            current_list = None
        else:
            result[key] = value.strip('"')
            current_list = None
    return result


def validate_internal_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "#")):
                continue
            clean = target.split("#", 1)[0]
            resolved = (path.parent / clean).resolve()
            if clean and not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link to {target}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    manifest = ROOT / "knowledge/00-Chef-OS-Manifest.md"
    if manifest.exists():
        manifest_text = manifest.read_text(encoding="utf-8")
        if len(re.findall(r"^System version:", manifest_text, re.MULTILINE)) != 1:
            errors.append("Manifest must declare exactly one System version")
        if "Current explicit user" not in manifest_text:
            errors.append("Manifest must preserve current-user authority")

    project_instructions = ROOT / "PROJECT-INSTRUCTIONS.md"
    if project_instructions.exists():
        word_count = len(project_instructions.read_text(encoding="utf-8").split())
        if word_count > 500:
            warnings.append(
                f"PROJECT-INSTRUCTIONS.md is {word_count} words; keep the router compact"
            )

    chef_rules = ROOT / "knowledge/03-Chef-Rules.md"
    if chef_rules.exists():
        rules_text = chef_rules.read_text(encoding="utf-8")
        for snippet in REQUIRED_CHEF_RULE_SNIPPETS:
            if snippet not in rules_text:
                errors.append(f"Chef Rules is missing required policy: {snippet}")

    recipe_paths = sorted((ROOT / "recipes").rglob("*.md"))
    if not recipe_paths:
        errors.append("No canonical recipe files found")

    seen_ids: dict[str, Path] = {}
    forbidden_name = re.compile(r"(?:^|[-_])(v\d+|final|copy|backup)(?:[-_.]|$)", re.I)

    for path in recipe_paths:
        relative = path.relative_to(ROOT)
        if forbidden_name.search(path.name):
            errors.append(f"{relative}: filename looks like version debris")
        text = path.read_text(encoding="utf-8")
        try:
            metadata = parse_front_matter(text, relative)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        missing = REQUIRED_METADATA - metadata.keys()
        if missing:
            errors.append(f"{relative}: missing metadata {sorted(missing)}")

        recipe_id = str(metadata.get("id", ""))
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", recipe_id):
            errors.append(f"{relative}: invalid recipe id {recipe_id!r}")
        elif recipe_id in seen_ids:
            errors.append(
                f"{relative}: duplicate id {recipe_id!r}, also in "
                f"{seen_ids[recipe_id].relative_to(ROOT)}"
            )
        else:
            seen_ids[recipe_id] = path

        status = str(metadata.get("status", ""))
        if status not in ALLOWED_STATUSES:
            errors.append(f"{relative}: unsupported status {status!r}")

        schema = str(metadata.get("schema_version", ""))
        if schema != "1":
            errors.append(f"{relative}: schema_version must be 1")

        headings = set(re.findall(r"^## (.+?)\s*$", text, re.MULTILINE))
        for section in REQUIRED_SECTIONS:
            if section not in headings:
                errors.append(f"{relative}: missing section '{section}'")

        if status == "draft" and "## Reliability note" not in text:
            warnings.append(f"{relative}: draft has no Reliability note")

    validate_internal_links(errors)

    print(f"Chef OS validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    if errors:
        return 1
    print(f"Validated {len(recipe_paths)} recipe file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
