import re

import typer

from cli.core.find import search_mac

app = typer.Typer()


def validate_mac(value: str) -> str:
    if len(value) not in [4, 12]:
        raise typer.BadParameter("Please enter the full or last 4 characters of the MAC address")
    mac = re.match(rf"^[a-fA-F0-9]{{{len(value)}}}$", value)
    if not mac:
        raise typer.BadParameter(f"Invalid MAC: {value}")
    return "-".join([value[i : i + 2] for i in range(0, len(value), 2)])


@app.command()
def mac(
    mac: str = typer.Argument(..., callback=validate_mac, help="Full or last 4 characters of the MAC address"),
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True, hide_input=True),
):
    """
    Find Desktop/Phone by MAC Address
    """
    device = search_mac(mac)
    typer.echo(device)
