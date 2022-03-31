import re

import typer
from rich.console import Console
from rich.table import Table

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
    devices = search_mac(mac, username, password)

    table = Table(title="Devices")
    table.add_column("Hostname")
    table.add_column("IP Address")
    table.add_column("MAC Address")
    table.add_column("Switch")
    table.add_column("Switch IP")
    table.add_column("Port")
    table.add_column("Link")
    table.add_column("Protocol")
    table.add_column("Last Input")
    table.add_column("Last Output")
    table.add_column("Input Errors")
    table.add_column("Output Errors")

    for device in devices:
        table.add_row(
            device["hostname"],
            device["ip"],
            device["mac"],
            device["switch"],
            device["switch_ip"],
            device["port"],
            device["link"],
            device["protocol"],
            device["last_input"],
            device["last_output"],
            device["input_errors"],
            device["output_errors"],
        )

    console = Console()
    console.print(table)
