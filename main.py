# Given a path to a text file and a two-letter ISO standard language code which the content would be translated to
# Generate a new text file with the translated content

from translate import Translator

to_lang = "ja"
translator = Translator(to_lang=to_lang)

with open("./text_files/snow_white.txt", mode="r") as file:
    content = file.read()

    translation = translator.translate(content)

print(translation)
