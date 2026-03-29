#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "diagrams" / "registry.json"


def main() -> int:
    data = json.loads(REGISTRY.read_text())
    for entry in data["diagrams"]:
        diagram_id = entry["id"]
        diagram_text = (ROOT / entry["file"]).read_text().rstrip()
        block = f'<!-- DIAGRAM: {diagram_id} START -->\n```mermaid\n{diagram_text}\n```\n<!-- DIAGRAM: {diagram_id} END -->'
        pattern = re.compile(
            rf"<!-- DIAGRAM: {re.escape(diagram_id)} START -->(.*?)<!-- DIAGRAM: {re.escape(diagram_id)} END -->",
            re.DOTALL,
        )
        for used_in in entry["used_in"]:
            path = ROOT / used_in
            original = path.read_text()
            updated, count = pattern.subn(block, original)
            if count != 1:
                raise SystemExit(f"marker mismatch for {diagram_id} in {used_in}")
            path.write_text(updated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
