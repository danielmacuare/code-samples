#!/usr/bin/env python3

"""
    This is a template to help you break down CLI APPs with typer
"""
from typer import Typer

import add
import delete
import discover
import show

app = Typer()
app.add_typer(add.app, name="add")
app.add_typer(delete.app, name="delete")
app.add_typer(discover.app, name="discover")
app.add_typer(show.app, name="show")


if __name__ == "__main__":
    app()
