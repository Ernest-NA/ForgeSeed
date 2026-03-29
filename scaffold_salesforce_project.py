#!/usr/bin/env python3
"""
Salesforce project scaffolder for ForgeSeed.
Creates a ready-to-use Salesforce repository skeleton from variants/salesforce/repo-template.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "variants" / "salesforce" / "repo-template"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "salesforce-project"


def replace_tokens(text: str, tokens: dict[str, str]) -> str:
    for key, value in tokens.items():
        text = text.replace(f"__{key}__", value)
    return text


def is_text_file(path: Path) -> bool:
    text_exts = {
        ".md", ".txt", ".yml", ".yaml", ".json", ".toml", ".ini", ".cfg",
        ".gitignore", ".editorconfig", ".ps1", ".bat", ".py", ".csv", ".xml"
    }
    return path.suffix.lower() in text_exts or path.name in {".gitignore", ".editorconfig", ".forceignore"}


def copy_template(template_root: Path, destination: Path, tokens: dict[str, str]) -> None:
    for source in template_root.rglob("*"):
        rel = source.relative_to(template_root)
        rel_parts = [replace_tokens(part, tokens) for part in rel.parts]
        target = destination.joinpath(*rel_parts)

        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue

        target.parent.mkdir(parents=True, exist_ok=True)

        if is_text_file(source):
            content = source.read_text(encoding="utf-8")
            target.write_text(replace_tokens(content, tokens), encoding="utf-8")
        else:
            shutil.copy2(source, target)


def try_git_init(project_dir: Path) -> None:
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "init"], cwd=project_dir, check=True)
    except Exception:
        print("Aviso: no se pudo inicializar git automáticamente.", file=sys.stderr)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scaffold a Salesforce project from ForgeSeed.")
    parser.add_argument("project_name", help="Human-readable project name.")
    parser.add_argument("--dest", default=".", help="Destination directory where the project folder will be created.")
    parser.add_argument("--description", default="New Salesforce project", help="Project description.")
    parser.add_argument("--author", default=os.environ.get("USERNAME", "Unknown"), help="Project owner or author.")
    parser.add_argument("--package-name", default=None, help="Optional Salesforce package name. Defaults to project slug.")
    parser.add_argument("--init-git", action="store_true", help="Initialize a git repository after scaffolding.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not TEMPLATE_DIR.exists():
        print(f"Template directory not found: {TEMPLATE_DIR}", file=sys.stderr)
        return 1

    project_slug = slugify(args.project_name)
    package_name = args.package_name or project_slug.replace("-", "_")
    dest_root = Path(args.dest).expanduser().resolve()
    project_dir = dest_root / project_slug

    if project_dir.exists():
        print(f"Error: destination already exists: {project_dir}", file=sys.stderr)
        return 2

    tokens = {
        "PROJECT_NAME": args.project_name,
        "PROJECT_SLUG": project_slug,
        "PROJECT_DESCRIPTION": args.description,
        "AUTHOR": args.author,
        "PACKAGE_NAME": package_name,
    }

    project_dir.mkdir(parents=True, exist_ok=False)
    copy_template(TEMPLATE_DIR, project_dir, tokens)

    if args.init_git:
        try_git_init(project_dir)

    print(f"Salesforce project created successfully: {project_dir}")
    print("Next steps:")
    print("  1. Open the folder in your IDE.")
    print("  2. Review AGENTS.md and docs/architecture/system-overview.md.")
    print("  3. Update sfdx-project.json and package.xml if needed.")
    print("  4. Authenticate to your org with sf CLI.")
    print("  5. Run validation commands and create the initial commit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
