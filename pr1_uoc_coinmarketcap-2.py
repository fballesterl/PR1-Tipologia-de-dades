# 29/10/2021
# PR1_UOC_coinmarketcap
# Autors: Francesc Ballester Lecina i Oriol Raurell Gan
# Web scraping www.coinmarketcap.com

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime

#Opció 1: Permet descarregar qualsevol registre entre els 100 primers però no les variacions:

url = "https://coinmarketcap.com/es/" 
page = requests.get(url)
soup = BeautifulSoup(page.content,'lxml')
tr_tags = soup.tbody.find_all('tr')

def llista_top100_criptomonedes(tr_tag):

    td_tags = tr_tag.find_all('td')

    # Per extreure les etiquetes dels primers 10 registres
    if (tr_tags.index(tr_tag))<10:
        td_tag=td_tags[2]
        div_in_td = td_tag.find_all('div', class_='sc-16r8icm-0 sc-1teo54s-1 dNOTPP') 
        nom2 = div_in_td[0].find_all('p', class_='q7nmo0-0 bogImm')
        nom = nom2[0].text
        simbol2 = div_in_td[0].find_all('p', class_='q7nmo0-0 krbrab coin-item-symbol')
        simbol= simbol2[0].text
        preu = td_tags[3].text
     
     # Per extreure les etiquetes dels registres entre el 10 i el 100
    else:    
        span=td_tags[2].a.find_all('span')
        nom = span[1].text
        simbol= span[2].text
        preu = td_tags[3].text
    
    # Retorn de dades
    return {
        'Simbol': simbol, 
        'Nom': nom, 
        'Preu' : preu,
        'Dia': datetime.now().strftime("%d/%m/%Y"),
        'Hora': datetime.now().strftime("%H:%M"),
          }

# Iterem per cada objecte i convertim en dataframe
llista_top100_criptomonedes = pd.DataFrame([llista_top100_criptomonedes(tr_tags[i]) for i in range(100)])
# Covertim a csv i descarreguem
llista_top100_criptomonedes.to_csv("llista_top100_criptomonedes.csv", index=False)
# Mostra en pantalla els resultats
print(llista_top100_criptomonedes)


# Opció 2: Permet descarregar les variacions però només dels primers 20 registres:

url_2 = "https://coinmarketcap.com/es/all/views/all/" 
page_2 = requests.get(url_2)
soup_2 = BeautifulSoup(page_2.content, features='lxml')
tr_tags_2 = soup_2.tbody.find_all('tr')

def llista_top20_criptomonedes(tr_tag):

    # Extreim les dades directament:
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
 
    # Retorn de dades:
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
        'Hora': datetime.now().strftime("%H:%M")
          }

# Iterem per cada objecte i convertim en dataframe
llista_top20_criptomonedes = pd.DataFrame([llista_top20_criptomonedes(tr_tags_2[i]) for i in range(20)])
# Covertim a csv i descarreguem
llista_top20_criptomonedes.to_csv("llista_top20_criptomonedes.csv", index=False)
# Mostra en pantalla els resultats
print(llista_top20_criptomonedes)


# Descàrrega en Colaboratory: from google.colab import files
'''files.download("llista_top100_criptomonedes")'''
'''files.download("llista_top20_criptomonedes")'''
