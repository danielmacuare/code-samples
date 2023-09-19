#!/usr/bin/env python3

"""
    Add Command: Used to add --discovered-devices or a --single-device to Netbox

    Usage:
        python main.py add --help
        python main.py add --discovered-devices
        python main.py add --single-device chi-leaf-04
        python main.py add -d
        python main.py add -s chi-leaf-04
"""

from typer import Option, Typer, echo

app = Typer(short_help="add --discovered-devices or a --single-device")


@app.callback("add", invoke_without_command=True)
def add_options(
    discovered_devices: bool = Option(
        False,
        "--discovered-devices",
        "-d",
        help="Discovered Devices into netbox",
    ),
    single_device: str = Option(
        None, "--single-device", "-s", help='Choose a scope: "subnet" OR "devices"'
    ),
) -> None:
    """Add Discovered Devices to Netbox or add a static device"""
    if discovered_devices and single_device:
        echo(f'All Discovered devices and: "{single_device}" will be added to Netbox')
        exit()

    if discovered_devices:
        echo("All Discovered devices will be added to Netbox")
    if single_device:
        echo(f'The device: "{single_device}" will be added to Netbox')


if __name__ == "__main__":
    app()
