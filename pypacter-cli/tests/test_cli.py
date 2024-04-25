from pathlib import Path

import pytest
from click.testing import CliRunner
from src.pypacter_cli.cli import detect_language_cli, help_cli, version_cli


def test_cli_help() -> None:
    runner = CliRunner()
    result = runner.invoke(help_cli, ["--help"])
    assert result.exit_code == 0
    assert "PyPacter" in result.output


def test_cli_version() -> None:
    runner = CliRunner()
    result = runner.invoke(version_cli, ["--version"])
    assert result.exit_code == 0
    assert "PyPacter" in result.output


def test_cli_detect_language_stdin() -> None:
    runner = CliRunner()
    result = runner.invoke(detect_language_cli, input='print("Hello, world!")\n')
    assert result.exit_code == 0
    assert "python" in result.output


@pytest.fixture()
def code_snippet_file(tmp_path):
    code = 'print("Hello, world!")\n'
    file_path = tmp_path / "snippet.py"
    file_path.write_text(code)
    return file_path


def test_detect_language_with_file(code_snippet_file):
    runner = CliRunner()
    result = runner.invoke(detect_language_cli, ["--file", str(code_snippet_file)])
    assert result.exit_code == 0
    assert "python" in result.output
