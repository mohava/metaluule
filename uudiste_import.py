__author__ = 'Kaspar K2ngsepp, Mihkel Kohava'
import random
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
    #print(soup)
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
    puhastatud = []
    for uudis in uudised:
        if len(uudis.split(" ")) < 3:
            pass
        s6nad = []
        for s6na in uudis.split(" "):
            if s6na in {"FOTOD", "VIDEO"}:
                pass
            else:
                s6nad.append(s6na)
        uudis = " ".join(s6nad)

        puhastatud.append(uudis)
    return puhastatud

def vali_uudis(uudised):
    uudis = random.choice(uudised)
    return uudis

def uudis2v6tmesõnad(uudis):
    v6tmesõnad = set()
    s6nad = uudis.strip().split(" ")
    for s6na in s6nad:
        if s6na in {"ja", "või"}:
            pass
        else:
            v6tmesõnad.add(s6na)
    return list(v6tmesõnad)

