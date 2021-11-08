# PR1_UOC_coinmarketcap
# Autors: Francesc Ballester Lecina i Oriol Raurell Gan
# Web scraping www.coinmarketcap.com

# Llibreries necessàries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


# Pàgina d'extracció de les dades
url = "https://coinmarketcap.com/es/all/views/all/" 
# Resposta a la petició
page = requests.get(url)
# Dades en brut de la pàgina web
soup = BeautifulSoup(page.content, features='lxml')
# Etiqueres "tr"
tr_tags = soup.tbody.find_all('tr') 

# Definició per retornar les dades d'una criptomoneda
# Exemple d'extracció per posició en el rank: cryptocurrency(tr_tags[0])
def cryptocurrency(tr_tag):

    # Etiquetes "td"
    td_tags = tr_tag.find_all('td')
   
    # Extracció de la informació disponible en la segona etiqueta "td"
    td_tag = td_tags[1]
    div_in_td = td_tag.find_all('div')
    a = div_in_td[0].find_all('a', class_='cmc-table__column-name--name cmc-link')
    # Extracció del nom de la criptomoneda
    nom = a[0].text
    # Extracció del enllaç per més informació
    base_url = 'https://coinmarketcap.com'
    url_criptomoneda = td_tag.a['href'].strip()
    URL = base_url + url_criptomoneda   
    
    # Extracció de la posició en el ranking
    rank = td_tags[0].text
    # Extracció del simbol
    simbol = td_tags[2].text
    # Extracció del total de capitalització
    cap = td_tags[3].find_all('span', class_='sc-1ow4cwt-1 ieFnWP')
    capital = cap[0].text
    # Extracció del preu
    preu = td_tags[4].text
    # Extracció del nombre d'unitats de la criptomoneda
    circulacio = td_tags[5].text
    # Extracció del valor de totes les unitats de la criptomoneda
    volum = td_tags[6].text
    # Extracció de la variació de preu en l'última hora
    h1 = td_tags[7].text.replace('.',',')
    # Extracció de la variació de preu en les últimes 24 hores
    h24 = td_tags[8].text.replace('.',',')
    # Extracció de la variació de preu en l'última setmana
    d7 = td_tags[9].text.replace('.',',')

    # Retorn amb el nom dels camps i el valor
    return {
        'Rank': rank,
        'Nom': nom, 
        'Simbol': simbol, 
        'Preu' : preu,
        'En circulacio' : circulacio,
        'Cap. de mercat' : capital,
        'Volum(24h)' : volum,
        '%1h' : h1,
        '%24h' : h24,
        '%7d' : d7,
        'url' : URL,
        'Dia': datetime.now().strftime("%d/%m/%Y"),
        'Hora': datetime.now().strftime("%H:%M")
          }

# Definició per iterar les etiquetes "tr" de cada criptomoneda del top20 i convertir en dataframe
def top20_cryptocurrencies():
    data_top20 = pd.DataFrame([cryptocurrency(tr_tags[i]) for i in range(20)])
    return data_top20

# Definició per convertir el dataset en un arxiu .csv sense index
def top20_cryptocurrencies_csvfile():
    top20_cryptocurrencies().to_csv('top_criptocurrencies.csv', index=False)

# Descàrrega en csv a la direcció C:/Usuari/
top20_cryptocurrencies_csvfile()
