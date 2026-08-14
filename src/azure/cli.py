"""Command line interface for azure-mist."""
import click


@click.group()
def main():
    """haze and fog image enhancement filters"""


@main.command()
def version():
    """Print version."""
    click.echo("azure-mist 0.4.1")


if __name__ == "__main__":
    main()
