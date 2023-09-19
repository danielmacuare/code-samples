#!/usr/bin/env python3

"""
    Source Code to create commands and options with Typer

    Usage:
        python main.py delete --help
        python main.py delete --all-devices --dry-run
        python main.py delete --single-device fra-fw-02
        python main.py delete -ad
        python main.py delete -s fra-fw-02

Links:
- Typer Commands: https://typer.tiangolo.com/tutorial/commands/
- Breaking Down CLI in Multiple Files: https://typer.tiangolo.com/tutorial/subcommands/add-typer/
- Callback invoke.. https://github.com/tiangolo/typer/issues/119#issuecomment-795654576
- Why add a callback: https://github.com/tiangolo/typer/issues/402

- "..." use the ellipsis in the Option when you want to have an optional to be required
but you don't want to provide a default value.
"""

from typer import Option, Typer, echo

app = Typer(short_help="delete --all or specific --device. --dry-run available ")


@app.callback("delete", invoke_without_command=True)
def delete_options(
    all_devices: bool = Option(
        False,
        "--all-devices",
        "-a",
        help="Delete all devices from Netbox",
    ),
    dry_run: bool = Option(
        False,
        "--dry-run",
        "-d",
        help="(Dry-run) Delete all devices from Netbox",
    ),
    single_device: str = Option(
        None, "--single-device", "-s", help='Choose a scope: "subnet" OR "devices"'
    ),
) -> None:
    """Delete all devices or a single device from Netbox. dry-run available"""
    if dry_run:
        echo("(DRY-RUN): The Devices selected will not be deleted from Netbox")
        if not all_devices and not single_device:
            echo("Please use one of the 2 options: --all-devices or --single-device")
            exit(1)

    if single_device:
        echo(f'The device: "{single_device}" will be deleted from Netbox')
        exit()

    if all_devices:
        echo("All devices will be deleted from Netbox")


if __name__ == "__main__":
    app()
