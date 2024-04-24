import argparse
from pypacter.language_detection import detect_language

def detect_language_from_file(file_path):
    """
    Detects the programming language from a code snippet file.

    Args:
        file_path (str): The path to the code snippet file.

    Returns:
        str: The detected programming language.
    """
    with open(file_path, 'r') as file:
        code_snippet = file.read()
    detected_language = detect_language(code_snippet)
    return detected_language

def detect_language_from_stdin():
    """
    Detects the programming language from a code snippet provided through standard input.

    Returns:
        str: The detected programming language.
    """
    code_snippet = input("Enter the code snippet: ")
    detected_language = detect_language(code_snippet)
    return detected_language

def main():
    """
    Main function to parse command-line arguments and execute the appropriate action.
    """
    parser = argparse.ArgumentParser(description="Detect the programming language of a code snippet.")
    parser.add_argument('source', choices=['file', 'stdin'], help="Specify the source of the code snippet.")
    parser.add_argument('--file-path', help="Path to the code snippet file (required if source is 'file').")

    args = parser.parse_args()

    if args.source == 'file':
        if not args.file_path:
            parser.error("File path is required when source is 'file'.")
        detected_language = detect_language_from_file(args.file_path)
    elif args.source == 'stdin':
        detected_language = detect_language_from_stdin()

    print("Detected language:", detected_language)

if __name__ == "__main__":
    main()
