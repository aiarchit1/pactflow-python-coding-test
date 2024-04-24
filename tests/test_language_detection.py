"""
Tests for the language detection functionality of the pypacter project.
"""

import pytest
from pypacter.language_detection import detect_language

def test_detect_language_python():
    """
    Test language detection for a Python code snippet.

    This test case verifies that the language detection function correctly identifies
    the programming language of a Python code snippet and returns 'Python'.
    """
    code_snippet = "def hello():\n    print('Hello, World!')"
    detected_language = detect_language(code_snippet)
    assert detected_language == "Python"

def test_detect_language_java():
    """
    Test language detection for a Java code snippet.

    This test case verifies that the language detection function correctly identifies
    the programming language of a Java code snippet and returns 'Java'.
    """
    code_snippet = "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"
    detected_language = detect_language(code_snippet)
    assert detected_language == "Java"

if __name__ == "__main__":
    pytest.main()
