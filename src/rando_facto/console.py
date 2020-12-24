import textwrap

import click

from . import __version__, wikipedia

API_URL: str = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """The rando facto hypermodern python project"""
    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))
