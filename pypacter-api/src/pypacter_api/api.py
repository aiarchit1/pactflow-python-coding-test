from flask import Flask, request, jsonify
from pypacter.language_detection import detect_language

app = Flask(__name__)

@app.route('/detect-language', methods=['POST'])
def detect_language():
    """
    Endpoint to detect the programming language of a code snippet.

    This endpoint accepts a POST request with a JSON object containing a code snippet.
    It then calls the detect_language from the pypacter core package to detect the language
    of the code snippet and returns the detected language in the response.

    Returns:
        JSON: A JSON object containing the detected programming language.
    """
    data = request.get_json()
    code_snippet = data.get('code_snippet')

    if not code_snippet:
        return jsonify({'error': 'Code snippet not provided'})

    detected_language = detect_language(code_snippet)
    return jsonify({'detected_language': detected_language})

if __name__ == '__main__':
    app.run(debug=True)
