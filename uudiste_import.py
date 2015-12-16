import requests
from bs4 import BeautifulSoup
#DELFI, ERR, PM, ÄRILEHT, NAISTEKAS??, ELU 24...
def improdi_uudised():
    r = requests.get("http://uudised.err.ee/uudised")
    soup = BeautifulSoup(r.content, "html.parser")
    #vanas6nad = soup.html.body.div.div.div.encode("utf-8")
    vanas6nad = soup.html.body.div.div.div.encode("utf-8")


    print(vanas6nad)
    #return pealkirjad # [{portaal, pealkiri, kommentaaride arv).....]


improdi_uudised()