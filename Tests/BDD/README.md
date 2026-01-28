# BDD Suite

This folder contains Gherkin-style feature files that describe the
principal DolphiniOS user journeys. The scenarios are used by the
BDD validation script in CI to ensure each scenario includes
Given/When/Then steps.

## Running locally

```
python3 scripts/bdd/validate_features.py
```

To view a concise console report (used in the VHS recording):

```
python3 scripts/bdd/run_bdd.py
```
