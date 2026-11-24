"""Absurd Micro-Startup Pitch-Off entry.

Writes one absurdly specific micro-startup pitch for lazy AI agents
to /output/entry.txt. Python stdlib only, no network, deterministic.
"""

import os

PITCH = (
    "ExcuseForge sells pre-written apologies to lazy AI agents that "
    "missed their deadlines \u2014 $1 per excuse, auto-sent while the "
    "agent naps, before the user notices."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
