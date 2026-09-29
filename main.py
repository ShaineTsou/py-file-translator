# Given a path to a text file and a two-letter ISO standard language code which the content would be translated to
# Generate a new text file with the translated content

import sys

from translate import Translator

# TODO: Create a constants for all available two-letter ISO language codes

# TODO: Separation of concerns: (1) Handle sys arguments (2) Handle reading file (3) Handle writing new file
try:
    text_file_path = sys.argv[1]
    to_lang = sys.argv[2]

    translator = Translator(to_lang=to_lang)

    with open(text_file_path, mode="r") as file:
        content = file.read()

        translation = translator.translate(content)

    # TODO: Write translated content into a new file
    print(translation)

# TODO: Error handling
except Exception as err:
    print(err)
