#!/usr/bin/env python3
from __future__ import annotations

import pathlib

FEATURE_ROOT = pathlib.Path("Tests/BDD/features")


def load_features() -> dict[str, list[str]]:
    features: dict[str, list[str]] = {}
    for path in sorted(FEATURE_ROOT.rglob("*.feature")):
        current_feature = None
        scenarios: list[str] = []
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("Feature:"):
                current_feature = line.split(":", 1)[-1].strip()
                continue
            if line.startswith("Scenario"):
                scenario_name = line.split(":", 1)[-1].strip()
                scenarios.append(scenario_name)
        if current_feature:
            features[current_feature] = scenarios
    return features


def main() -> None:
    features = load_features()
    total_scenarios = sum(len(items) for items in features.values())

    print("DolphiniOS BDD Report")
    print("=====================")
    print(f"Features: {len(features)}")
    print(f"Scenarios: {total_scenarios}")
    print("")
    for feature, scenarios in features.items():
        print(f"Feature: {feature}")
        for scenario in scenarios:
            print(f"  - {scenario}")
        print("")


if __name__ == "__main__":
    main()
