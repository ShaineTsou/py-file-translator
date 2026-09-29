# Given a path to a text file and a two-letter ISO standard language code which the content would be translated to
# Generate a new text file with the translated content

import sys

from translate import Translator

# TODO: Create a constants for all available two-letter ISO language codes

# TODO: Separation of concerns: (2) Handle reading file (3) Handle writing new file

SYS_ARGS_ERR_MSG = "Error: Please provide text file path and desired language. Usage: python3 main.py [text_file_path] [to_lang]"


def get_sys_args():
    try:
        text_file_path = sys.argv[1]
        to_lang = sys.argv[2]

        return text_file_path, to_lang
    except IndexError:
        print(SYS_ARGS_ERR_MSG)
    except Exception as err:
        print(f"Error: {err}")


def get_content(text_file_path):
    if not text_file_path:
        return

    try:
        with open(text_file_path, mode="r") as file:
            return file.read()
    except FileNotFoundError:
        print(SYS_ARGS_ERR_MSG)
    except Exception as err:
        print(f"Error: {err}")


def main():
    try:
        text_file_path, to_lang = get_sys_args()
        content = get_content(text_file_path)

        translator = Translator(to_lang=to_lang)
        translation = translator.translate(content)

        # TODO: Write translated content into a new file
        print(translation)
    except TypeError:
        print(SYS_ARGS_ERR_MSG)
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
