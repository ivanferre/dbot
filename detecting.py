#!/usr/bin/python

from googletrans import Translator

text1 = '''
A Római Birodalom (latinul Imperium Romanum) az ókori Róma által létrehozott 
államalakulat volt a Földközi-tenger medencéjében
'''

text2 = '''
Vysoké Tatry sú najvyššie pohorie na Slovensku a v Poľsku a sú zároveň jediným 
horstvom v týchto štátoch s alpským charakterom. 
'''

text3 = '''
Si els homes escriuen llibres, només és per poder unir-se als altres éssers humans més enllà del propi alè i, d'aquesta manera, defensar-se davant l'implacable antagonista de la vida: la caducitat i l'oblit. 
'''

translator = Translator()

dt1 = translator.detect(text1)
print(dt1)

dt2 = translator.detect(text2)
print(dt2)

dt3 = translator.detect(text3)
print(dt3)
