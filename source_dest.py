#!/usr/bin/python

from googletrans import Translator

translator = Translator()

translated = translator.translate('svízelná situace', src='cs', dest='hu')

print(translated.text)
