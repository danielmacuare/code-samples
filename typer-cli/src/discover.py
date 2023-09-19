#!/usr/bin/env python3

"""
    Source Code to create commands and Options with Typer
    Breaking Down CLI in Multiple Files: https://typer.tiangolo.com/tutorial/subcommands/add-typer/
    CLI Options: https://typer.tiangolo.com/tutorial/options/

    Usage:
        python main.py discover --help
        python main.py discover subnet 10.1.1.0/24
        python main.py discover device chi-leaf-04
"""

from typer import Typer, echo

app = Typer(short_help="discover a subnet or discover a device")


@app.command("subnet")
def discover_subnet(
    subnet: str,
) -> None:
    """Discover devices on a subnet"""
    echo(f"Discovering Devices on subnet: {subnet}")


@app.command("device")
def discover_device(
    device: str,
) -> None:
    """Discover a specific device"""
    echo(f"Discovering Device: {device}")
