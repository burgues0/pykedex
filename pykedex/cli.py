"""Module that provides the Pykedex CLI"""

import asyncio, aiopoke, time
import typer, json
from pathlib import Path
from typing import Optional
from pykedex import __app_name__, __version__
# from rich import print




app = typer.Typer()
PROJECT_DIR = Path().resolve()
JSON_CONTENT_DIR = PROJECT_DIR / "data"

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

#defines main as a typer callback
@app.callback()
def main(
    #version argument defaults to typer.Option object - allows to create command line options
    version: Optional[bool] = typer.Option(
        None,                                               #starts the default option value as none
        "--version",                                        #sets the cli names for the "version" option (--version or -v)
        "-v",   
        help="Show the application's version and exit.",    #help message for the version option
        callback=_version_callback,                         #attaches its respective callback function (running the version option will callback to _version_callback())
        is_eager=True,                                      #version command has precedence over other commands
    )
) -> None:
    return

@app.command()
def pokedex(

) -> None:
    return

@app.command()
def moves() -> None:
    print("ok")

@app.command()
def abilities(

) -> None:
    return

@app.command()
def items(

) -> None:
    return

@app.command()
def typechart(

) -> None:
    return

@app.command()
def nature():
    file = json.load(open(JSON_CONTENT_DIR / "natures.json"))
    for nature in file:
        print(nature)

@app.command()
def tools(

) -> None:
    return

@app.command()
def create(username: str):
    print(f"Creating user: {username}")