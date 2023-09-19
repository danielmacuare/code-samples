#!/usr/bin/env python3

from typer import Typer

import add
import delete
import discover
import show

app = Typer()
app.add_typer(show.app, name="show")
app.add_typer(discover.app, name="discover")
app.add_typer(add.app, name="add")
app.add_typer(delete.app, name="delete")


if __name__ == "__main__":
    app()
