from typing import Optional

import typer

from commands import find
from utils.version import get_version

app = typer.Typer(add_completion=False)
app.add_typer(find.app, name="find")

def version_callback(value: bool):
    if value:
        typer.echo(f"Version: {get_version()}")
        raise typer.Exit()

@app.callback()
def version(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True, help="Returns CLI version"
    )
):
    pass


if __name__ == "__main__":
    app()