from __future__ import annotations

import subprocess
from pathlib import Path


def run_git(
    args: list[str],
    cwd: Path,
) -> None:
    subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
    )


def initialize_repository(
    directory: Path,
) -> None:
    run_git(
        ["init", "-b", "main"],
        directory,
    )


def create_initial_commit(
    directory: Path,
) -> None:
    run_git(
        ["add", "."],
        directory,
    )

    run_git(
        [
            "commit",
            "-m",
            "feat: initialize service from golden path",
        ],
        directory,
    )


def add_remote(
    directory: Path,
    repository_url: str,
) -> None:
    run_git(
        [
            "remote",
            "add",
            "origin",
            repository_url,
        ],
        directory,
    )


def push(
    directory: Path,
) -> None:
    run_git(
        [
            "push",
            "-u",
            "origin",
            "main",
        ],
        directory,
    )