import typer

app = typer.Typer()


@app.command()
def mac(mac: str):
    """
    Find Desktop/Phone by MAC Address
    """
    pass