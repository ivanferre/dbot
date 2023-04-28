#!/usr/bin/python

from googletrans import Translator

translator = Translator()

data = ['Dobrý deň', 'majestátny orol', 'krehká dohoda']

# Original example provided by https://zetcode.com/python/googletrans/
# * It crashes, somehow.
# translated = translator.translate(data, src='sk', dest='ca')
# for trans in translated:
#     print('Translating...')
#     print(f'{trans.origin} -> {trans.text}')

for d in data:
    translated = translator.translate(d, src='sk', dest='ca')
    print (f'{translated.origin} -> {translated.text}')
