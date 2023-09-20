#!/usr/bin/env python3

"""
    Show Command: Used to show devices and subnets available in Netbox or the Local DB

    Usage:
        python main.py show --help
        python main.py show netbox --help
        python main.py show netbox devices
        python main.py show netbox subnets
        python main.py show local --help
        python main.py show local devices
        python main.py show local subnets
"""

from typer import Argument, Typer, echo

app = Typer(short_help='Options: "Local" or "Netbox"')


@app.command("local")
def show_local(
    scope: str = Argument(help='Choose a scope: "subnets" OR "devices"'),
) -> None:
    """Show devices and subnets available in the local DB"""
    echo(f"Show {scope} available in the local Database")


@app.command("netbox")
def show_netbox(
    scope: str = Argument(help='Choose a scope: "subnets" OR "devices"'),
) -> None:
    """Show devices and subnets available in Netbox"""
    echo(f"Show {scope} available in Netbox")


if __name__ == "__main__":
    app()
