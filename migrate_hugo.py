# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "rich",
# ]
# ///

import os
import shutil
from pathlib import Path
import click
from rich.console import Console

console = Console()

@click.command()
@click.argument("directory", type=click.Path(exists=True))
def migrate(directory):
    """Converts flat Hugo .md files into Page Bundles (index.md)."""
    base_path = Path(directory)
    
    # Find all .md files that aren't already index.md or _index.md
    md_files = [
        f for f in base_path.glob("*.md") 
        if f.stem not in ["index", "_index"]
    ]

    if not md_files:
        console.print("[yellow]No files found to migrate.[/yellow]")
        return

    for file_path in md_files:
        # Create a folder with the name of the post
        new_folder = base_path / file_path.stem
        new_folder.mkdir(exist_ok=True)
        
        # Move the .md file to the new folder as index.md
        destination = new_folder / "index.md"
        shutil.move(str(file_path), str(destination))
        
        console.print(f"[green]Migrated:[/green] {file_path.name} -> {new_folder.name}/index.md")

    console.print(f"\n[bold green]Success![/bold green] Migrated {len(md_files)} posts.")

if __name__ == "__main__":
    migrate()
