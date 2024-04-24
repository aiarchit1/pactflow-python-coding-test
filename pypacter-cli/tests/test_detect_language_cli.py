"""
Tests for the CLI functionality of the pypacter project.
"""

import subprocess
import os
import pytest


def test_detect_language_from_file():
    """
    Test the CLI command to detect the programming language from a code snippet file.

    This test creates a temporary file with a code snippet, executes the CLI command,
    captures the output, and checks if the detected language matches the expected result.
    """
    # Create a temporary file with a code snippet
    code_snippet = "def hello():\n    print('Hello, World!')"
    file_path = 'test_code.py'
    with open(file_path, 'w') as file:
        file.write(code_snippet)

    # Execute the CLI command and capture the output
    output = subprocess.check_output(['python', 'detect_language_cli.py', 'file', '--file-path', file_path])
    output = output.decode('utf-8').strip()

    # Cleanup the temporary file
    os.remove(file_path)

    # Check if the detected language matches the expected result
    assert output == 'Python'


def test_detect_language_from_stdin():
    """
    Test the CLI command to detect the programming language from standard input.

    This test executes the CLI command, provides input data, captures the output,
    and checks if the detected language matches the expected result.
    """
    # Prepare input data
    input_data = "def hello():\n    print('Hello, World!')"

    # Execute the CLI command and provide input data
    process = subprocess.Popen(['python', 'detect_language_cli.py', 'stdin'], stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = process.communicate(input=input_data.encode('utf-8'))
    output = stdout.decode('utf-8').strip()

    # Check if the detected language matches the expected result
    assert output == 'Python'


if __name__ == "__main__":
    pytest.main()
