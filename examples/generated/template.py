## Generated template on 2024-08-06 21:09:20.460271
from typing import Optional, Any
import typer
import subprocess
GLOBAL_VAR = 'hello'


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
cli = typer.Typer(context_settings=CONTEXT_SETTINGS)
__version__ = '0.1.0'
__cli_name__ = 'template'


def version_callback(value: bool):
    if value:
        print(f"{__cli_name__}, {__version__}")
        raise typer.Exit()

@cli.callback()
def main(
    version: Optional[bool] = typer.Option(None, '--version', callback=version_callback, is_eager=True)
):
    pass


@cli.command("hello")
def hello(local_arg: str = typer.Argument(...), local_arg_2: str = typer.Option("")):
    subprocess.run(["hello",f"""{local_arg}""","--" + f"""{local_arg_2}"""])


if __name__ == "__main__":
    cli()
