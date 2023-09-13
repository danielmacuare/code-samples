#!/usr/bin/env python3

"""
    Source Code to create commands and sub-commands

    Usage:
        python 1-show.py show netbox devices
        python 1-show.py show netbox subnets
        python 1-show.py show discovered subnets
        python 1-show.py show discovered subnets
"""

from typer import Argument, Typer, echo

app = Typer()
show = Typer(short_help='Options: "Netbox" or "Discovered"')
app.add_typer(show, name="show")


@show.command("discovered")
def show_discovered(
    scope: str = Argument(help='Choose a scope: "subnet" OR "devices"'),
) -> None:
    """Show Devices Discovered"""
    echo(f"show discovered {scope.lower()}")


@show.command("netbox")
def show_netbox(
    scope: str = Argument(help='Choose a scope: "subnet" OR "devices"'),
) -> None:
    """Show Devices in Netbox"""
    echo(f"show netbox {scope.lower()}")


if __name__ == "__main__":
    app()
