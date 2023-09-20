#!/usr/bin/env python3

"""
    Delete Command: Used to delete --all-devices or a --single device from Netbox

    Usage:
        python main.py delete --help
        python main.py delete --all-devices --dry-run
        python main.py delete --single-device fra-fw-02
        python main.py delete -ad
        python main.py delete -s fra-fw-02
"""

from typer import Option, Typer, colors, echo, secho

app = Typer(
    short_help="delete --all-devices or a --single-device from Netbox. --dry-run available"
)


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
        echo("(DRY-RUN): The Devices will NOT be deleted. Ignore the message below:")
        if not all_devices and not single_device:
            secho(
                "ERROR 1: Please use one of the 2 options: --all-devices or --single-device",
                fg=colors.RED,
            )
            exit(1)

    if single_device:
        echo(f'The device: "{single_device}" has been deleted from Netbox')
        exit()

    if all_devices:
        echo("All devices have been deleted from Netbox")


if __name__ == "__main__":
    app()
