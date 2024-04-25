"""
Tests for the language detection functionality of the pypacter project.
"""

import pytest
from src.pypacter import language_detection

def test_detect_language_python() -> None:
    """
    Test language detection for a Python code snippet.

    This test case verifies that the language detection function correctly identifies
    the programming language of a Python code snippet and returns 'python'.
    """
    code_snippet = "def hello():\n    print('Hello, World!')"
    detected_language = language_detection.detect_language(code_snippet)
    assert len(detected_language) > 0
    assert "python" in detected_language

def test_detect_language_java() -> None:
    """
    Test language detection for a Java code snippet.

    This test case verifies that the language detection function correctly identifies
    the programming language of a Java code snippet and returns 'java'.
    """
    code_snippet = """public class Main {\n    public static void main(String[] args)
    {\n        System.out.println(\"Hello, World!\");\n    }\n}"""
    detected_language = language_detection.detect_language(code_snippet)
    assert len(detected_language) > 0
    assert "java" in detected_language

def test_detect_language_javascript() -> None:
    """
    Test language detection for a javascript code snippet.

    This test case verifies that the language detection function correctly identifies
    the programming language of a javascript code snippet and returns 'javascript'.
    """
    code_snippet = """
            console.log("Hello, World!");
             """
    detected_language = language_detection.detect_language(code_snippet)
    assert len(detected_language) > 0
    assert "javascript" in detected_language

