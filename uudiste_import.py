__author__ = 'Kaspar K2ngsepp, Mihkel Kohava'
import random
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

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

def improdi_uudised2():
    r = requests.get('http://www.delfi.ee/archive/viimased/')
    soup = BeautifulSoup(r.content, "html.parser")

    parssimataUudised= soup.find_all("a", href=True)
    uudisedLingid = []
    for uudis in parssimataUudised:
        link = uudis["href"]
        uudis = uudis.get_text().strip()
        uudisedLingid.append((uudis, link))
    return uudisedLingid

def puhasta(uudised):
    puhastatud = []
    for uudis in uudised:
        if len(uudis.split(" ")) < 3 or len(uudis)<9:
            pass
        else:
            s6nad = []
            for s6na in uudis.split(" "):
                if s6na in {"FOTOD:", "VIDEO:", "GRAAFIK:"}:
                    pass
                else:
                    s6nad.append(s6na)
            uudis = " ".join(s6nad)
            puhastatud.append(uudis)
    return puhastatud

def puhasta2(uudisedLingid):
    puhastatud = []
    for uudis, link in uudisedLingid:
        if len(uudis.split(" ")) < 3 or len(uudis)<9:
            pass
        else:
            s6nad = []
            for s6na in uudis.split(" "):
                if s6na in {"FOTOD:", "VIDEO:", "GRAAFIK:"}:
                    pass
                else:
                    s6nad.append(s6na)
            uudis = " ".join(s6nad)
            puhastatud.append((uudis, link))
    return puhastatud

def vali_uudis(uudisedLingid):
    uudisLink = random.choice(uudisedLingid)
    return uudisLink

def uudis2v6tmesõnad(uudis):
    v6tmesõnad = []
    s6nad = uudis.strip().split(" ")
    for s6na in s6nad:
        if s6na in {"ja", "või"}:
            pass
        else:
            v6tmesõnad.append(s6na)
    return list(v6tmesõnad)

def uudis2v6tmesõnad2(uudisLink):
    uudis, link = uudisLink
    v6tmesõnad = []
    s6nad = uudis.strip().split(" ")
    for s6na in s6nad:
        if s6na in {"ja", "või"}:
            pass
        else:
            v6tmesõnad.append(s6na)
    return list(v6tmesõnad)

print(uudis2v6tmesõnad2(vali_uudis(puhasta2(improdi_uudised2()))))
#print(puhasta(["Kohver"]))

