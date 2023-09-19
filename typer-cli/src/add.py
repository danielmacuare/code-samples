#!/usr/bin/env python3

"""
    Source Code to create commands and sub-commands with Typer

    Usage:
        python main.py add --help
        python main.py add --discovered-devices
        python main.py add --single-device chi-leaf-04
        python main.py add -d
        python main.py add -s chi-leaf-04

Links:
- Typer Commands: https://typer.tiangolo.com/tutorial/commands/
- Breaking Down CLI in Multiple Files: https://typer.tiangolo.com/tutorial/subcommands/add-typer/
- Callback invoke.. https://github.com/tiangolo/typer/issues/119#issuecomment-795654576
- Why add a callback: https://github.com/tiangolo/typer/issues/402

- "..." use the ellipsis in the Option when you want to have an optional to be required
but you don't want to provide a default value.
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
    static_device: str = Option(
        None, "--single-device", "-s", help='Choose a scope: "subnet" OR "devices"'
    ),
) -> None:
    """Add Discovered Devices to Netbox or add a static device"""
    if discovered_devices and static_device:
        echo(f'All Discovered devices and: "{static_device}" will be added to Netbox')

        exit()

    if discovered_devices:
        echo("All Discovered devices will be added to Netbox")
    if static_device:
        echo(f'The static device: "{static_device}" will be added to Netbox')


if __name__ == "__main__":
    app()
