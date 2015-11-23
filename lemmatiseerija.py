import requests
from bs4 import BeautifulSoup
#http://www.filosoft.ee/lemma_et/
def lemmatiseeri(sona):
    sõnatyved = set()
    r = requests.get('http://www.filosoft.ee/lemma_et/lemma.cgi?word=' +sona.encode("utf-8"))
    soup = BeautifulSoup(r.content, "html.parser")
    try:
        tyved = soup.body.br.get_text().split("\n")
    except:
        print("Tühi sõne sisendiks.")
        return set()
    for element in tyved:
        if element != "" and element != "Copyright © 2013":
            sõnatyved.add(element)
    return sõnatyved #vahel on s6navormil mitu sobivat tüve kasin: kasima ja kasin

#print(lemmatiseeri(""))
