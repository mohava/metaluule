import requests
from bs4 import BeautifulSoup
'''#defineeri siia funktisoon, mis võtab sisendiks sõna ja tagastab listi,
#  kus on kõik päringust saadud vanasõnad (iga vanasõna on listi üks element) '''

#def kysi_vanas6nad(sõna):
sona = "naine"

r = requests.post('http://www.folklore.ee/cgi-bin/script1', data = {"entry":sona})
print(r.content) # selline html-kood on r.content -is


soup = BeautifulSoup(r.content, "html.parser")
#print(soup.prettify())
#print(soup.body.table.get_text())
print(soup.body.table.get_text()) #ma proovin seda veel normaalsemale kujule saada

