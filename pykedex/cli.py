"""Module that provides the Pykedex CLI"""

import asyncio, aiopoke, time
import typer, json
from rich.console import Console
from rich.table import Table
from pathlib import Path
from typing import Optional
from pykedex import __app_name__, __version__

app = typer.Typer()
appConsole = Console()
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
def pokedex() -> None:
    """
    Displays all of the avaliable Pokémon in the National Dex order (all 1008).
    """    
    return

@app.command()
def moves() -> None:
    """
    Displays all of the avaliable Pokémon moves.
    """    
    print("ok")

@app.command()
def abilities() -> None:
    """
    Displays all of the avaliable Pokémon abilities.
    """    
    return

@app.command()
def items() -> None:
    """
    Displays all of the avaliable usable items in the digital franchise.
    """    
    return

@app.command()
def typechart() -> None:
    """
    Displays the Type Effectiveness Chart.
    """
    return

@app.command()
def nature():
    """
    Displays all of the avaliable Pokémon natures.
    """
    file = json.load(open(JSON_CONTENT_DIR / "natures.json"))
    natureTable = Table(title="Pokémon Natures")
    natureTable.add_column("Nature")
    natureTable.add_column("Increases", style="green")
    natureTable.add_column("Decreases", style="red")
    for nature in file:
        natureTable.add_row(str(nature).capitalize(), str(file[nature]['increased_stat']), str(file[nature]['decreased_stat']))
    appConsole.print(natureTable)

@app.command()
def tools() -> None:
    return