from typer.testing import CliRunner
from pykedex import __app_name__, __version__, cli

runner = CliRunner()

#version unit test
def test_version():
    result = runner.invoke(cli.app, ["--version"])                  #calls .invoke() on runner to run it with the --version option
    assert result.exit_code == 0                                    #asserts that the app ran successfully (exit code 0)
    assert f"{__app_name__} v{__version__}\n" in result.stdout      #asserts that the app version is present in the std output (result.stdout)