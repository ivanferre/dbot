from googletrans import Translator


translator = Translator(service_urls=[
 	'translate.google.com',
])
translator = Translator()

data = str(open('first-post.md', encoding='utf8', newline='\n').read())
# print(data)
translations = translator.translate([data], src='en', dest='fa')
print(translations)
print(translations._response.http_version)

for translation in translations:
	print(translation.origin, ' -> ', translation.text)
