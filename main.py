# Given a path to a text file and a two-letter ISO standard language code which the content would be translated to
# Generate a new text file with the translated content

import sys

from translate import Translator
from translate.exceptions import TranslationError

# TODO: Create a constants for all available two-letter ISO language codes

# TODO: Separation of concerns: (2) Handle reading file (3) Handle writing new file


def get_sys_args():
    text_file_path = sys.argv[1]
    to_lang = sys.argv[2]

    return text_file_path, to_lang


def get_content(text_file_path):
    if not text_file_path:
        return

    with open(text_file_path, mode="r") as file:
        return file.read()


def get_translation(content, to_lang):
    if not content or not to_lang:
        return

    translator = Translator(to_lang=to_lang)
    translation = translator.translate(content)
    return translation


def main():
    try:
        text_file_path, to_lang = get_sys_args()
        content = get_content(text_file_path)

        if not content or not to_lang:
            return
        else:
            translation = get_translation(content, to_lang)
            # TODO: Write translated content into a new file
            print(translation)
    except FileNotFoundError, IndexError, TypeError:
        print(
            "Error: Please provide text file path and desired language. Usage: python3 main.py [text_file_path] [to_lang]"
        )
    except TranslationError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
