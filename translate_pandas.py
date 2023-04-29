#/usr/bin/python3

# This file is to replicate
# https://medium.com/analytics-vidhya/translate-list-and-pandas-data-frame-using-googletrans-library-in-python-f28b8cb84f21


# ! TODO install pandas
# https://pandas.pydata.org/getting_started.html
# https://docs.continuum.io/free/anaconda/install/

from googletrans import Translator
import pandas as pd

# I have created a pandas data frame and will be translating that into English.

translator = Translator()
df = pd.DataFrame({'Spanish':['piso','cama']})
df

