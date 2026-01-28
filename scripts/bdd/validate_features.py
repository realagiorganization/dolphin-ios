#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import sys

FEATURE_ROOT = pathlib.Path("Tests/BDD/features")


def _iter_feature_files() -> list[pathlib.Path]:
    if not FEATURE_ROOT.exists():
        return []
    return sorted(FEATURE_ROOT.rglob("*.feature"))


def _clean_line(line: str) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return ""
    return stripped


def validate_feature(path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    feature_found = False
    scenario = None
    scenario_steps: dict[str, set[str]] = {}

    def finalize_scenario(name: str | None) -> None:
        if not name:
            return
        steps = scenario_steps.get(name, set())
        missing = {"Given", "When", "Then"} - steps
        if missing:
            errors.append(
                f"{path}: Scenario '{name}' missing steps: {', '.join(sorted(missing))}"
            )

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = _clean_line(raw_line)
        if not line:
            continue
        if line.startswith("Feature:"):
            feature_found = True
            continue
        if line.startswith("Scenario"):
            finalize_scenario(scenario)
            scenario = line.split(":", 1)[-1].strip() or "(unnamed)"
            scenario_steps[scenario] = set()
            continue
        if line.split()[0] in {"Given", "When", "Then"}:
            if scenario is None:
                errors.append(f"{path}: Step found before any Scenario")
            else:
                scenario_steps[scenario].add(line.split()[0])

    finalize_scenario(scenario)

    if not feature_found:
        errors.append(f"{path}: Missing Feature header")
    if not scenario_steps:
        errors.append(f"{path}: No Scenario definitions found")

    return errors


def main() -> int:
    feature_files = _iter_feature_files()
    if not feature_files:
        print("No feature files found.")
        return 1

    errors: list[str] = []
    for feature in feature_files:
        errors.extend(validate_feature(feature))

    if errors:
        print("BDD validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"BDD validation passed for {len(feature_files)} feature files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
