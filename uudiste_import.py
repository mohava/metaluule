__author__ = 'Kaspar K2ngsepp, Mihkel Kohava'

import requests
from bs4 import BeautifulSoup
#DELFI, ERR, PM, ÄRILEHT, NAISTEKAS??, ELU 24...
def improdi_uudised():
    #r = requests.get("http://uudised.err.ee/uudised")
    # soup = BeautifulSoup(r.content, "html.parser")
    # #uudised = soup.html.body.div.div.div.encode("utf-8")
    # #uudised = soup.ul.li.get_text().encode("utf-8")
    r = requests.get('http://www.delfi.ee/archive/viimased/')
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup)
    #uudised = soup.body.ol.li.div.a.get_text() #saab ainult ühe uudise
    uudised = soup.body.ol.get_text().strip()
    list = uudised.split('\n')
    hulk = set()
    for element in list:
        if element == '':
            pass
        elif element[0] == '\t' or element[0].isdigit():
            pass
        else:
            hulk.add(element)
    return hulk
    #return pealkirjad # [{portaal, pealkiri, kommentaaride arv).....]


def puhasta(uudised):
    puhastatud = set()
    for uudis in uudised:
        if len(uudis.split(" ")) < 3:
            pass
        else:
            puhastatud.add(uudis)
    return puhastatud

uudised = improdi_uudised()
for uudis in puhasta(uudised):
    print(uudis)

