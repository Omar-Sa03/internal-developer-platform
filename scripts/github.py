from __future__ import annotations

import os
import subprocess


def create_repository(
    repository_name: str,
    description: str,
    visibility: str = "public",
) -> str:
    """Create a GitHub repository and return its URL."""

    if visibility not in {"public", "private"}:
        raise ValueError(
            "visibility must be 'public' or 'private'"
        )

    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")

    if not token:
        raise RuntimeError(
            "GH_TOKEN or GITHUB_TOKEN must be set."
        )

    command = [
        "gh",
        "repo",
        "create",
        repository_name,
        f"--{visibility}",
        "--description",
        description,
    ]

    environment = os.environ.copy()
    environment["GH_TOKEN"] = token

    result = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )

    return result.stdout.strip()