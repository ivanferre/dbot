#/usr/bin/python3
#
# testGoogletrans
# test the API Googletrans
# https://py-googletrans.readthedocs.io/en/latest/
#
# assumes the module has been installed with
#   pip install googletrans

import googletrans
from googletrans import Translator
translator = Translator(service_urls=[
 	'translate.google.com',
])
translator = Translator()

# If source language is not given, google translate attempts to detect the source language.
#translator.translate('안녕하세요.')
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
flagSentence = translator.translate('Una bandera ens agermana!', dest='en', src='ca')
print(flagSentence.text)

# Array can be used to translate a batch of strings in a single method call and a single HTTP session. The exact same method shown above work for arrays as well.
#translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ca')
#for translation in translations:
#    print(translation.origin, ' -> ', translation.text)

english = ['The quick brown fox', 'jumps over', 'the lazy dog']
for s in english:
    ca = translator.translate(s, src='en', dest='ca')
    print(f'{ca.origin} -> {ca.text}')

print("That's all, folks!")
