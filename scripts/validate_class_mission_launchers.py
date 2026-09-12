from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MISSIONS = ROOT / "02_Class_Missions"
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ROW_RE = re.compile(r"^\|\s*(\d{1,3})\s*\|")

# Exact Session 1–78 coverage belongs to the preserved compatibility route.
PHASE_NAMES = (
    "00_Orientation_and_Evidence",
    "Legacy_01_CS50P_Python",
    "Legacy_02_NumPy_Pandas_Visualisation",
    "Legacy_03_Bohrium_ML_Foundations",
    "Legacy_04_AI_History_and_Thinking_Humans",
    "05_Andrew_Ng_ML_Model_Labs",
    "06_Andrew_Ng_DL_PyTorch",
    "07_Model_Comparison_EDA_Evaluation",
    "08_Tuning_Ensembling_Competition",
)
PHASES = [MISSIONS / name for name in PHASE_NAMES]


def main() -> int:
    errors: list[str] = []
    sessions: list[int] = []
    packet_count = 0

    for phase in PHASES:
        if not phase.exists():
            errors.append(f"Missing compatibility phase: {phase.relative_to(ROOT)}")
            continue
        launcher = phase / "SESSION_LAUNCHER.md"
        if not launcher.exists():
            errors.append(f"Missing launcher: {phase.relative_to(ROOT)}")
            continue
        for line in launcher.read_text(encoding="utf-8").splitlines():
            match = ROW_RE.match(line)
            if not match:
                continue
            session = int(match.group(1))
            sessions.append(session)
            local_md = 0
            for _label, raw in LINK_RE.findall(line):
                if raw.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = raw.split("#", 1)[0].strip()
                if not target:
                    continue
                resolved = (launcher.parent / target).resolve()
                if resolved.suffix.lower() != ".md":
                    continue
                local_md += 1
                packet_count += 1
                if not resolved.exists():
                    errors.append(f"Broken Session {session} link: {raw}")
                    continue
                try:
                    resolved.relative_to(phase.resolve())
                except ValueError:
                    errors.append(f"Session {session} target is outside its compatibility Phase: {resolved.relative_to(ROOT)}")
            if local_md == 0:
                errors.append(f"Session {session} has no phase-local Markdown packet")

    if sessions != list(range(1, 79)):
        errors.append(f"Expected compatibility Sessions 1–78 exactly once; found {sessions}")

    if errors:
        print("Class Missions launcher validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Class Missions compatibility launcher validation passed.")
    print("Legacy Session coverage: Sessions 1–78 exactly once")
    print(f"Phase-local lesson links: {packet_count}")
    print("Current IOAI unit order is validated separately from legacy session numbering.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())