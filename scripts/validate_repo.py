#!/usr/bin/env python3
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def fail(message: str) -> None:
    raise SystemExit(message)


def validate_required_files() -> None:
    required = [
        ROOT / "AGENTS.md",
        ROOT / "CONTEXT.md",
        ROOT / "docs" / "architecture.md",
        ROOT / "twin" / "digital-twin.yaml",
        ROOT / "twin" / "capabilities.md",
        ROOT / "twin" / "input-contracts.md",
        ROOT / "twin" / "output-contracts.md",
        ROOT / "twin" / "memory-policy.md",
        ROOT / "deployments" / "templates" / "deployment-template.yaml"
    ]
    for path in required:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT)}")


def validate_registry() -> None:
    registry = json.loads((ROOT / "diagrams" / "registry.json").read_text())
    for entry in registry["diagrams"]:
        if not (ROOT / entry["file"]).exists():
            fail(f"missing diagram file: {entry['file']}")


def main() -> int:
    validate_required_files()
    validate_registry()
    print("repo validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
