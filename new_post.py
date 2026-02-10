# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "rich",
# ]
# ///

"""
Hugo Post Creator for HackWimbledon.
Creates a new Page Bundle with YAML front matter and opens the editor.
"""

import datetime
from pathlib import Path
import click
from rich.console import Console

console = Console()


def get_yaml_template(title: str) -> str:
    """Returns a standard YAML front matter block."""
    date_str = datetime.datetime.now().isoformat(timespec="seconds")
    return f"""---
title: "{title}"
date: {date_str}
draft: true
---

Write your content here...
"""


@click.command()
@click.argument("title")
def create_post(title: str):
    """
    Create a new Hugo post bundle in content/news/ and open the editor.
    """
    # Create slug from title
    slug = title.lower().replace(" ", "-")
    post_dir = Path(f"content/news/{slug}")

    if post_dir.exists():
        console.print(f"[bold red]Error:[/bold red] Directory {post_dir} already exists!")
        return

    # Create the bundle structure
    post_dir.mkdir(parents=True)
    (post_dir / "images").mkdir()
    index_file = post_dir / "index.md"

    # Write the initial content
    content = get_yaml_template(title)
    index_file.write_text(content, encoding="utf-8")

    console.print(f"[green]✓[/green] Created post bundle at [bold]{post_dir}[/bold]")
    console.print("[blue]Opening editor...[/blue]")

    # Opens the file in the system default editor
    click.edit(filename=str(index_file))


if __name__ == "__main__":
    create_post()
