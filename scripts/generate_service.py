from pathlib import Path
import shutil
import sys

from jinja2 import Environment, FileSystemLoader


TEMPLATE_DIR = Path("templates/python-fastapi/skeleton")
OUTPUT_BASE = Path("generated")


def generate_service(service_name: str, team: str, environment: str, github_owner: str) -> Path:
    output_dir = OUTPUT_BASE / service_name

    if output_dir.exists():
        raise FileExistsError(
            f"Service already exists: {output_dir}"
        )

    output_dir.mkdir(parents=True)

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR)
    )

    values = {
    "service_name": service_name,
    "team": team,
    "environment": environment,
    "github_owner": github_owner,
    "replicas": 1,
    "image_repository": (
        f"ghcr.io/{github_owner}/{service_name}"
    ),
    "image_tag": "latest",
}

    for source in TEMPLATE_DIR.rglob("*"):
        if source.is_dir():
            continue

        relative_path = source.relative_to(TEMPLATE_DIR)

        template = env.get_template(
            relative_path.as_posix()
        )

        rendered = template.render(values=values)

        destination = output_dir / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)

        destination.write_text(
            rendered,
            encoding="utf-8",
        )

    return output_dir


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python scripts/generate_service.py "
            "<service_name> <team> <environment> <github_owner>"
        )
        sys.exit(1)

    generate_service(
    service_name=sys.argv[1],
    team=sys.argv[2],
    environment=sys.argv[3],
    github_owner=sys.argv[4],
)

    print(f"Service '{sys.argv[1]}' generated successfully.")