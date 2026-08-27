from __future__ import annotations

import subprocess
from pathlib import Path


def apply_application(
    manifest: Path,
) -> None:
    """Create or update an Argo CD Application."""

    subprocess.run(
        [
            "kubectl",
            "apply",
            "-f",
            str(manifest),
        ],
        check=True,
    )