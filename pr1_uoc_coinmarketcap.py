# -*- coding: utf-8 -*-
"""PR1_UOC_coinmarketcap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c0iOT6K1UjLPaw6jGXJWWj6RLFyNuiO6
"""

# Dades extretes de la pàgina principal, ordenades per valor de capitalitzció de mercat
# Les etiquetes canvien a partir del registre 10
# Les dades de variacions diaries i setmanals no incorporen el signe, depenen de la classe (no s'han incorporat)
# Les hores en colaboratory surten 2h abans, en canvi en VisualCode surt correctament.


import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime

url = "https://coinmarketcap.com/es/" 
page = requests.get(url)
soup = BeautifulSoup(page.content,'lxml')
tr_tags = soup.tbody.find_all('tr')

def complete_cryptocurrencies_list(tr_tag):

    td_tags = tr_tag.find_all('td')

    if (tr_tags.index(tr_tag))<10:
        td_tag=td_tags[2]
        div_in_td = td_tag.find_all('div', class_='sc-16r8icm-0 sc-1teo54s-1 dNOTPP') 
        name2 = div_in_td[0].find_all('p', class_='q7nmo0-0 bogImm')
        name = name2[0].text
        symbol2 = div_in_td[0].find_all('p', class_='q7nmo0-0 krbrab coin-item-symbol')
        symbol= symbol2[0].text
        price_in_USD = td_tags[3].text
    else:    
        span=td_tags[2].a.find_all('span')
        name = span[1].text
        symbol= span[2].text
        price_in_USD = td_tags[3].text
    return {
        'Cryptocurrency': symbol, 
        'Name': name, 
        'Price_in_USD' : price_in_USD,
        'Date': datetime.now().strftime("%d/%m/%Y"),
        'Hour': datetime.now().strftime("%H:%M"),
          }

top_100_cryptocurrenices = pd.DataFrame([complete_cryptocurrencies_list(tr_tags[i]) for i in range(100)])
top_100_cryptocurrenices

#Opció 2

# Dades extretes de la pàgina https://coinmarketcap.com/es/all/views/all/, ordenades per valor de capitalitzció de mercat
# Les etiquetes canvien a partir del registre 20, ja que s'ha de baixar la pagina perque s'actualitzi el format i es mostrin mes

url_2 = "https://coinmarketcap.com/es/all/views/all/" 
page_2 = requests.get(url_2)
soup_2 = BeautifulSoup(page_2.content)
tr_tags_2 = soup_2.tbody.find_all('tr')

def complete_cryptocurrencies_list_2(tr_tag):

    td_tags = tr_tag.find_all('td')
    td_tag = td_tags[1]
    div_in_td = td_tag.find_all('div') 
    a = div_in_td[0].find_all('a', class_='cmc-table__column-name--name cmc-link')
    nom = a[0].text
    simbol = td_tags[2].text
    cap = td_tags[3].find_all('span', class_='sc-1ow4cwt-1 ieFnWP')
    capital = cap[0].text
    preu = td_tags[4].text
    circulacio = td_tags[5].text
    volum = td_tags[6].text
    h1 = td_tags[7].text
    h24 = td_tags[8].text
    d7 = td_tags[9].text
    
    return {
        'Nom': nom, 
        'Simbol': simbol, 
        'Cap. de mercat' : capital,
        'Preu' : preu,
        'En circiulació' : circulacio,
        'Volum(24h)' : volum,
        '%1h' : h1,
        '%24h' : h24,
        '%7d' : d7,
        'Dia': datetime.now().strftime("%d/%m/%Y"),
        'Hour': datetime.now().strftime("%H:%M")
          }
top_100_cryptocurrenices_2 = pd.DataFrame([complete_cryptocurrencies_list_2(tr_tags_2[i]) for i in range(20)])
top_100_cryptocurrenices_2

## 23/10/2021:

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime
from google.colab import files


url_2 = "https://coinmarketcap.com/es/all/views/all/" 
page_2 = requests.get(url_2)
soup_2 = BeautifulSoup(page_2.content, features='lxml')
tr_tags_2 = soup_2.tbody.find_all('tr')

def complete_cryptocurrencies_list_2(tr_tag):

    td_tags = tr_tag.find_all('td')
    rank = td_tags[0].text
    td_tag = td_tags[1]
    div_in_td = td_tag.find_all('div')
    a = div_in_td[0].find_all('a', class_='cmc-table__column-name--name cmc-link')
    nom = a[0].text
    simbol = td_tags[2].text
    cap = td_tags[3].find_all('span', class_='sc-1ow4cwt-1 ieFnWP')
    capital = cap[0].text
    preu = td_tags[4].text
    circulacio = td_tags[5].text
    volum = td_tags[6].text
    h1 = td_tags[7].text.replace('.',',')
    h24 = td_tags[8].text.replace('.',',')
    d7 = td_tags[9].text.replace('.',',')
    base_url = 'https://coinmarketcap.com'
    url_criptomoneda = td_tag.a['href'].strip()
    URL = base_url + url_criptomoneda   
 
    return {
        'Rank': rank,
        'Nom': nom, 
        'Simbol': simbol, 
        'Cap. de mercat' : capital,
        'Preu' : preu,
        'En circulacio' : circulacio,
        'Volum(24h)' : volum,
        '%1h' : h1,
        '%24h' : h24,
        '%7d' : d7,
        'url' : URL,
        'Dia': datetime.now().strftime("%d/%m/%Y"),
        'Hour': datetime.now().strftime("%H:%M")
          }

top_100_cryptocurrenices_2 = pd.DataFrame([complete_cryptocurrencies_list_2(tr_tags_2[i]) for i in range(20)])
print(top_100_cryptocurrenices_2)

## Descarga en local machine (Visual Code, Pycharm..):
'''top_100_cryptocurrenices_2.to_csv("cryptocurrenices_2.csv", index=False)
top_100_cryptocurrenices_2'''

## Descarga en Colaboratory:
'''top_100_cryptocurrenices_2.to_csv("cryptocurrenices_2.csv", index=False)
files.download("cryptocurrenices_2.csv")'''