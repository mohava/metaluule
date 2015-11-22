import requests
from bs4 import BeautifulSoup
#http://www.filosoft.ee/lemma_et/
def lemmatiseeri(s6na):
    sõnatüved = set()
    r = requests.get('http://www.filosoft.ee/lemma_et/lemma.cgi?word=' +s6na)
    soup = BeautifulSoup(r.content, "html.parser")
    try:
        tüved = soup.body.br.get_text().split("\n")
    except:
        print("Tühi sõne sisendiks.")
        return set()
    for element in tüved:
        if element != "" and element != "Copyright © 2013":
            sõnatüved.add(element)
    return sõnatüved #vahel on s6navormil mitu sobivat tüve kasin: kasima ja kasin

print(lemmatiseeri("tegemata"))
