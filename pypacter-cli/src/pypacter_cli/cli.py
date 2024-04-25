"""
Detects the language of a code snippet using CLI.
"""

import click

from src.pypacter import language_detection


@click.command()
@click.option("--file", type=click.Path(exists=True),
              help="Path to a file containing the code snippet")
def detect_language_cli(file: str) -> str:
    """
    Detects the programming language from a code snippet file.

    Args:
        file (str): The path to the code snippet file.

    Returns:
        str: The detected programming language.
    """
    if file:
        with open(file, "r") as f:
            code_snippet = f.read()
    else:
        # Read from standard input
        code_snippet = click.get_text_stream("stdin").read()

    # Called language detection function
    detected_language = language_detection.detect_language(code_snippet)

    click.echo(f"Detected language: {detected_language}")
    return detected_language


@click.command()
@click.option("--help",
              help="To get the help for PyPacter")
def help_cli() -> str:
    """
    To get the help for PyPacter.
    """
    return """ PyPacter has two option for CLI:
    1.--file:
        python language_detection_cli.py --file path/to/code_snippet.py
    2.Direct code snippet standard input like below.
        echo "print('Hello, world!')" | python language_detection_cli.py
        """


@click.command()
@click.option("--version",
              help="To get the version of PyPacter")
def version_cli() -> str:
    """
    To get the version of PyPacter.
    """
    from src.pypacter.util import get_version
    version = get_version()
    return f"Version of PyPacter: {version}"
