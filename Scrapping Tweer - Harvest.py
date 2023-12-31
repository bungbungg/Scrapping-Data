# -*- coding: utf-8 -*-
"""Salinan dari Crawling Harvest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EFNmju9m9kYSFZve0ZbLp2gysD6V4CpH
"""

!pip install pandas
!curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
!sudo apt-get install -y nodejs

# Crawl Data

filename = 'kurikulum.csv'
search_keyword = 'kurikulum merdeka until:2022-12-31 since:2022-12-01 lang:id'
limit = 100

!npx --yes tweet-harvest@latest -o "{filename}" -s "{search_keyword}" -l {limit} --token ""

import pandas as pd

'''Tentukan jalur ke file CSV Anda'''

file_path = f"tweets-data/{filename}"

''' Baca file CSV ke dalam pandas '''
df = pd.read_csv(file_path, delimiter=";")
display(df)

# Cek jumlah data yang didapatkan

num_tweets = len(df)
print(f"Jumlah tweet dalam dataframe adalah {num_tweets}.")