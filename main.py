# Given a path to a text file and a two-letter ISO standard language code which the content would be translated to
# Generate a new text file with the translated content

import sys
from datetime import date
from pathlib import Path

from translate import Translator
from translate.exceptions import TranslationError


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


def get_translation_file_path(original_path, to_lang):
    file_path = Path(original_path)

    if not file_path.exists() or not file_path.is_file() or not to_lang:
        return

    today = date.today()

    target_path = (
        f"./translation_files/{file_path.stem}_{to_lang}_{today.strftime('%d%m%y')}.txt"
    )

    # Create parent directory if the parent directory doesn't exist
    Path(target_path).parent.mkdir(parents=True, exist_ok=True)

    return target_path


def create_translation_file(translation, original_path, to_lang):
    if not translation or not to_lang:
        return

    translation_file_path = get_translation_file_path(original_path, to_lang)

    try:
        with open(translation_file_path, mode="w") as file:
            file.write(translation)
    except Exception as err:
        print(f"Error: {err}")


def main():
    try:
        text_file_path, to_lang = get_sys_args()
        content = get_content(text_file_path)
        translation = get_translation(content, to_lang)
        create_translation_file(translation, text_file_path, to_lang)
    except FileNotFoundError, IndexError, TypeError:
        print(
            "Error: Please provide text file path and target language. Usage: python3 main.py [text_file_path] [to_lang]"
        )
    except TranslationError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
