import textwrap

import click

from . import __version__, wikipedia

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language):
    """The rando facto hypermodern python project"""
    data = wikipedia.random_page(language=language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))