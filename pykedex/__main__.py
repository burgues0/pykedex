from pykedex import cli, __app_name__

def main():
    #calling the typer app, passing the app name to the prog_name argument
    cli.app(prog_name = __app_name__)

if __name__ == "__main__":
    main()