# README Translate

## API Choice

- [LibreTranslate](https://libretranslate.com/): API key costs $29/month, and the reports point to poor translation quality, and platform not very stable.

- [Google Translation AI](https://cloud.google.com/translate) offers a trial period, and then the cost is per-use.

- [DeepL](https://www.deepl.com/es/blog/announcing-python-client-library-for-deepl-api) offers a free tier.

Other APIs:

- <https://www.abstractapi.com/guides/best-translation-apis-for-developers>
- <https://stackoverflow.com/questions/57189358/free-api-similar-to-google-translate-for-python>

## Google Developer

[Googletrans: Free and Unlimited Google translate API for Python](https://py-googletrans.readthedocs.io/en/latest/)

<https://developers.google.com/>

[Cloud Translation Documentation](https://cloud.google.com/translate/docs)

- <https://console.cloud.google.com/freetrial/signup/>
- <https://console.cloud.google.com/getting-started>
- <https://cloud.google.com/translate/docs/setup?hl=es_419>
- <https://cloud.google.com/translate/docs/setup>

## DeepL

Yet to explore.

## Adventures on Googletrans

Install it from PyPI:

    pip install googletrans

Successfully performed all tests in  <https://zetcode.com/python/googletrans/>
The translation of lists of strings does not work, but it is possible (see translate_list.py) to iterate on the list to do the same job.

<!-- TODO
    https://medium.com/analytics-vidhya/translate-list-and-pandas-data-frame-using-googletrans-library-in-python-f28b8cb84f21

    This requires Pandas:
            https://pandas.pydata.org/getting_started.html
            https://docs.continuum.io/free/anaconda/install/
 -->
