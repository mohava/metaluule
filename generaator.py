__author__ = 'Mihkel'
from vanas6nade_import import kysi_vanas6nad
from collections import defaultdict
from random import randint
from lemmatiseerija import lemmatiseeri
from lyhendaja import lyhenda
from parafraseerija import parafraseeriLaused
from syntesaator import synteseeri
from copy import deepcopy

def leia_vanas6nade_parameetrid(v6tmes6nad, uued_vanas6nad, originaals6na=True, parafraseeritud=False):
    parameetrid=defaultdict(list)
    if type(v6tmes6nad)==str:
        v6tmes6nad = {v6tmes6nad}

    for idNumber, vanas6na, levik in uued_vanas6nad:

        v6tmes6na = list(v6tmes6nad)[0]
        for s6na in v6tmes6nad:
            if s6na in vanas6na:
                v6tmes6na = s6na

        vanas6na = vanas6na.lower()
        vanas6na = lyhenda(vanas6na)

        ##BUG
        #print("võtmed",v6tmes6nad)
        #print("SÕNA",s6na)
        #print(v6tmes6na,"!!!!", vanas6na)

        try:
            s6na_asetus = vanas6na.index(v6tmes6na)
        except:
            s6na_asetus = 0
        v6tmes6na_t2pselt_kujul = (" "+v6tmes6na+" ") in vanas6na
        vanas6na_pikkus = len(vanas6na)
        parameetrid[vanas6na] = [s6na_asetus, vanas6na_pikkus, originaals6na, levik, v6tmes6na_t2pselt_kujul, parafraseeritud, idNumber]
    return parameetrid

#kood on kirjutatud pidades silmas, et siina vahel saaks olla kaalude optimeerimise funktsioon
#kaalud = kaalud()

#KAALUD: võtmesõna indeks, vanasõna pikkus, juhuslikkus, leidub sõna esialgsel kujul (mitte lemma), vanas6na levik,
#       v6tmesõna suhteline asetus, võtmesõna täpsel kujul (mitte sõna osana)
def leia_parim_vanas6na(parameetrid, kasutatud, kaalud=[-0.5,-0.7, 0.5, 0.2, 0.5, -0.5, 0.2, -0.5]):
    #print(kaalud)
    print("tik-tok")
    skoorid = []
    for vanas6na in parameetrid:
        s6na_indeks, vanas6na_pikkus, originaals6na, levik, v6tmes6na_t2psel_kujul, parfraseeritud, idNumber = parameetrid[vanas6na]
        skoor = s6na_indeks*kaalud[0] + vanas6na_pikkus*kaalud[1] + randint(0,100)*kaalud[2] \
                    + originaals6na*100*kaalud[3] + levik*kaalud[4] + s6na_indeks/vanas6na_pikkus*100*kaalud[5] \
                    + v6tmes6na_t2psel_kujul*100*kaalud[6] + parfraseeritud*kaalud[7]*100
        skoorid.append((skoor, vanas6na, idNumber))
    skoorid = sorted(skoorid, reverse=1)

    i = 0
    for skoor,parim_vanas6na, idNumber in skoorid:
        i += 1
        if idNumber not in kasutatud:
            kasutatud.append(idNumber)
            return parim_vanas6na, kasutatud
        if i == len(skoorid):
            return ("luuletus sai läbi", kasutatud)
    return ("luuletus sai läbi", kasutatud)

def kirjuta_rida(v6tmes6na, kaalud, kasutatud):
    #print("TÄHELEPANU!! võtmesõna: ",v6tmes6na)
    vanas6nad = kysi_vanas6nad(v6tmes6na)
    parameetrid = leia_vanas6nade_parameetrid(v6tmes6na, vanas6nad)
    lisaparameetrid = leia_vanas6nade_parameetrid(v6tmes6na, parafraseeriLaused(vanas6nad, v6tmes6na), parafraseeritud=True)
    lisaparameetrid = dict(lisaparameetrid)
    parameetrid.update(lisaparameetrid)
    rida, kasutatud = leia_parim_vanas6na(parameetrid, kasutatud, kaalud)


    if rida == "luuletus sai läbi":
        lemmad = list(lemmatiseeri(v6tmes6na))
        v6tmes6nad = deepcopy(lemmad)
        for lemma in lemmad:
            #print("syntimisele!!!", lemma)
            v6tmes6nad += list(synteseeri(lemma))
        v6tmes6nad = set(v6tmes6nad)
        #print("võtmesõnad!!!!",v6tmes6nad)
        v6tmes6nad.add(v6tmes6na)

        vanas6nad = []
        for v6tmes6na in v6tmes6nad:
            #print(vanas6nad)
            #print("update OK")
            vanas6nad += kysi_vanas6nad(v6tmes6na)
            
        parameetrid = leia_vanas6nade_parameetrid(v6tmes6nad, vanas6nad, originaals6na=False, parafraseeritud=False)
        parameetrid = dict(parameetrid)
        lisaparameetrid = leia_vanas6nade_parameetrid(v6tmes6nad, parafraseeriLaused(vanas6nad, v6tmes6nad), originaals6na=False, parafraseeritud=True)
        lisaparameetrid = dict(lisaparameetrid)
        parameetrid.update(lisaparameetrid)
        rida, kasutatud = leia_parim_vanas6na(parameetrid, kasutatud, kaalud)
        #print("RIDA",rida)

    s6nad = rida.split()
    viimane_s6na = s6nad[-1]
    return rida, viimane_s6na, kasutatud

def tee_luuletus(v6tmes6na, kaalud=[-0.5,-0.7, 0.5, 0.2, 0.5, -0.5, 0.2, -0.5], tekst=[""], loendur=0, ridu=12, kasutatud=[]):
    loendur +=1
    if loendur == ridu:
        return tekst
    if tekst[-1] == "luuletus sai läbi":
        eeltekst = tekst.remove("luuletus sai läbi")
        return eeltekst
    rida, viimane_s6na, kasutatud = kirjuta_rida(v6tmes6na, kaalud, kasutatud)
    tekst.append(rida)
    v6tmes6na = viimane_s6na.strip(".")
    tee_luuletus(v6tmes6na, kaalud, tekst, loendur, ridu, kasutatud)
    return tekst

#TEHA: fraaside järjekorra ümber tõstimne TEHTUD
#TEHA: mitmeharuline rekursioon (kogu luuletuse skoori arvutamine)
#TEHA: parima luuletuse esitamine
#TEHA: kui ei leia viimast sõna siis lisada rida "viimane sõna, sünonüüm"
#TEHA: kui ei leia viimast sõna siis lisada rida "viimane sõna, riimuv sõna" kus riimuv sõna on sama lõpu ja silpide arvuga
#TEHA: kontrollide, ega enne olnud võtmesõnad, ei esine uuesti
#TEHA: salvestada päringute tulemused anmbaasi: päritud võtmesõnad ja vanasõnad
#THEA: normaliseerida  iga seti skoorid
#TEHA: features: riimub? sama pikkus mis eelmisel?
#TEHA: internetiühendus GUIsse, numbrite äre kadumine TÖÖS

###MAIN###
"""
luuletus = tee_luuletus("kolm", ridu=12)
for line in luuletus:
    print(line)
"""