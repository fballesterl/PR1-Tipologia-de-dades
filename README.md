# PR1-Tipologia-de-dades

## Descripció

Extreu informació sobre les 20 criptomonedes més importants del mercat. La informació s'extreu de la pàgina web [Cryptocurrency Market Capitalizations](https://coinmarketcap.com/es/all/views/all/).

## Membres de la PR1

Francesc Ballester Lecina i Oriol Raurell Gan.

## Arxius

* `cryptocurrenices_2.csv`: Conjunt de dades generat.
* `pr1_uoc_coinmarketcap.py`: Fitxer amb la implementació de web scraping desenvolupat en python.

## Conjunt de dades

* `Nom`: Nom de la criptomoneda. 
* `Simbol`: Simbol de la criptomoneda. 
* `Cap. de mercat` : Valor de capitalització de mercat.
* `Preu` : Preu de la criptomoneda en dolars.
* `En circiulació` : Nombre de criptomonedes que hiha en circulació.
* `Volum(24h)` : Volum de dolars tractat en les 24h.
* `%1h` : Variació del preu de la criptomoneda en 1h.
* `%24h` : Variació del preu de la criptomoneda en 24h.
* `%7d` : Variació del preu de la criptomoneda respecte la setmana anterior.
* `Dia`: Dia de la extracció.
* `Hour`: Hora de la extracció.

## Requeriments

Per executar l'script és necessari instal·lar previament les següents biblioteques:

```
$ install requests
$ install beautifulsoup4
$ install pandas
$ install json
```
