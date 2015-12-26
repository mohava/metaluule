import requests
from bs4 import BeautifulSoup
import re
# http://www.filosoft.ee/gene_et/

#Mihkli debug
def puhasta(s6natyved):
    uuedtyved=[]
    for s6natyvi in s6natyved:
        uued = re.split("\\xa0|####", s6natyvi)
        for uus in uued:
            uuedtyved.append(uus)
    uuedtyved = set(uuedtyved)
    if uuedtyved == {""}:
        uuedtyved = {}
    return uuedtyved

def synteseeri(lemma): # teine parameeter vorm, sest siis peab
# läbi käima ainult nii palju kui vaja, mitte kõik
    s6natyved = []
    vormid = ['sg g', 'sg p']
# jätan vormidesse AINULT omastava ja osastava käände!! pole rohkem vaja muidu kulub päringute tegemiseks KAUEM AEGA
    # vormid = ['sg g', 'sg p', 'sg in, mas', 'sg el, mast', 'sg all', 'sg ad', 'sg abl', 'sg tr, maks', 'sg ter', 'sg es', 'sg ab, mata' , 'sg kom']
    ### võtan vormidest 'sg ill, adt' ehk sisseütl testimiseks välja sest see tagastab kaks vormi
    for element in vormid:
        r = requests.post('http://www.filosoft.ee/gene_et/gene.cgi', data = {'word': lemma, 'gi': element})
        soup = BeautifulSoup(r.content, "html.parser")
        # lemmad = soup
        try:
            lemmad = soup.body.table.br.get_text()  # töötab kui panna üks vorm gi: sisse, ehk peab tegema eraldi vormide jaoks uuesti läbi
        except:
            print("Tühi/vigane sõne lemmatiseerijas.")
            return '' # või return lemma
        s6natyved.append(lemmad.strip())

    #MIHKLI DEBUG
    s6natyved = puhasta(s6natyved)

    print("synteseeritud",s6natyved)
    return set(s6natyved)
print(synteseeri('nurjas'))

#print(synteseeri(12)) # tagastab listi ['12', '12']