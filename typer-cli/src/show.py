#!/usr/bin/env python3

"""
    Source Code to create commands and sub-commands with Typer
    Breaking Down CLI in Multiple Files: https://typer.tiangolo.com/tutorial/subcommands/add-typer/
    Typer Commands: https://typer.tiangolo.com/tutorial/commands/

    Usage:
        python show.py show --help
        python show.py show netbox --help
        python show.py show netbox devices
        python show.py show netbox subnets
        python show.py show discovered --help
        python show.py show discovered devices
        python show.py show discovered subnets
"""

from typer import Argument, Typer, echo

app = Typer(short_help='Options: "Discovered" or "Netbox"')


@app.command("discovered")
def show_discovered(
    scope: str = Argument(help='Choose a scope: "subnet" OR "devices"'),
) -> None:
    """Show Devices Discovered"""
    echo(f"show discovered {scope.lower()}")


@app.command("netbox")
def show_netbox(
    scope: str = Argument(help='Choose a scope: "subnet" OR "devices"'),
) -> None:
    """Show Devices in Netbox"""
    echo(f"show netbox {scope.lower()}")


if __name__ == "__main__":
    app()
