"""
Tests for the API functionality of the pypacter project.
"""

import json
import pytest
from flask import Flask
from pypacter_api.api import app

@pytest.fixture
def client():
    """
    Fixture to create a test client for the Flask application.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_detect_language_with_valid_code_snippet(client):
    """
    Test the /detect-language endpoint with a valid code snippet.

    This test sends a POST request to the /detect-language endpoint with a valid code snippet
    and checks if the response status code is 200, if the response contains the detected language,
    and if it matches the expected language.
    """
    code_snippet = "def hello():\n    print('Hello, World!')"
    response = client.post('/detect-language', json={'code_snippet': code_snippet})
    assert response.status_code == 200
    data = response.get_json()
    assert 'detected_language' in data
    assert data['detected_language'] == 'Python'


def test_detect_language_with_missing_code_snippet(client):
    """
    Test the /detect-language endpoint when the code snippet is missing.

    This test sends a POST request to the /detect-language endpoint without providing a code snippet
    and checks if the response status code is 400, and if the response contains the appropriate error message.
    """
    response = client.post('/detect-language', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Code snippet not provided'


if __name__ == "__main__":
    pytest.main()
