from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader


TEMPLATE_DIR = Path("platform/argocd")


def render_application(
    service_name: str,
    github_owner: str,
    output: Path,
) -> Path:
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR)
    )

    template = env.get_template(
        "application-template.yaml"
    )

    rendered = template.render(
        values={
            "service_name": service_name,
            "github_owner": github_owner,
        }
    )

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output.write_text(
        rendered,
        encoding="utf-8",
    )

    return output