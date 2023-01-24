"""Module that provides the Pykedex CLI"""

import typer
from typing import Optional
from pykedex import __app_name__, __version__
from apicalls import main

app = typer.Typer()

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
def moves(

) -> None:
    return

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
def natures() -> None:
    return

@app.command()
def tools(

) -> None:
    return