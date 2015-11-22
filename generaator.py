__author__ = 'Mihkel'
from vanas6nade_import import kysi_vanas6nad
from collections import defaultdict
from random import randint
from lemmatiseerija import lemmatiseeri
from lyhendaja import lyhenda

#parameetrid: sõna asetus, vanasõna pikkus
def leia_vanas6nade_parameetrid(v6tmes6na, uued_vanas6nad, originaals6na):
    parameetrid=defaultdict(list)
    for idNumber, vanas6na, levik in uued_vanas6nad:
        vanas6na = vanas6na.lower()
        vanas6na = lyhenda(vanas6na)
        s6na_asetus = vanas6na.index(v6tmes6na)
        v6tmes6na_t2pselt_kujul = (" "+v6tmes6na+" ") in vanas6na
        vanas6na_pikkus = len(vanas6na)
        parameetrid[vanas6na] = [s6na_asetus, vanas6na_pikkus, originaals6na, levik, v6tmes6na_t2pselt_kujul]
    return parameetrid

#kood on kirjutatud pidades silmas, et siina vahel saaks olla kaalude optimeerimise funktsioon

#KAALUD: võtmesõna indeks, vanasõna pikkus, juhuslikkus, leidub sõna esialgsel kujul (mitte lemma), vanas6na levik,
#  v6tmesõna suhteline asetus, võtmesõna täpsel kujul
def leia_parim_vanas6na(parameetrid, eeltekst, kaalud=[-0.5,-0.7, 0.1, 1, 0.1, -0.5, 0.1]):
    skoorid = []
    for vanas6na in parameetrid:
        s6na_indeks, vanas6na_pikkus, originaals6na, levik, v6tmes6na_t2psel_kujul = parameetrid[vanas6na]
        skoor = s6na_indeks*kaalud[0] + vanas6na_pikkus*kaalud[1] + randint(0,100)*kaalud[2] \
                    + originaals6na*100*kaalud[3] + levik*kaalud[4] + s6na_indeks/vanas6na_pikkus*100*kaalud[5] \
                    + v6tmes6na_t2psel_kujul*100*kaalud[6]
        skoorid.append((skoor, vanas6na))
    skoorid = sorted(skoorid, reverse=1)
    i = 0
    for skoor,parim_vanas6na in skoorid:
        i += 1
        if parim_vanas6na not in eeltekst:
            return parim_vanas6na
        if i == len(skoorid):
            return ("luuletus sai läbi")
    return ("luuletus sai läbi")

def kirjuta_rida(v6tmes6na, eeltekst):
    print("võtmesõna: ",v6tmes6na)
    vanas6nad = kysi_vanas6nad(v6tmes6na)
    parameetrid = leia_vanas6nade_parameetrid(v6tmes6na, vanas6nad, True)
    rida = leia_parim_vanas6na(parameetrid, eeltekst)
    if rida == "luuletus sai läbi":
        #print("lemma", v6tmes6na)
        v6tmes6nad = lemmatiseeri(v6tmes6na)
        #print("lemma2", v6tmes6na)
        for v6tmes6na in v6tmes6nad:
            vanas6nad = kysi_vanas6nad(v6tmes6na)
            parameetrid = leia_vanas6nade_parameetrid(v6tmes6na, vanas6nad, False)
            rida = leia_parim_vanas6na(parameetrid, eeltekst)
    s6nad = rida.split()
    viimane_s6na = s6nad[-1]
    return rida, viimane_s6na

def tee_luuletus(v6tmes6na, eeltekst=[""], loendur=0, ridu=12):
    loendur +=1
    if loendur == ridu:
        return eeltekst
    if eeltekst[-1] == "luuletus sai läbi":
        eeltekst = eeltekst.remove("luuletus sai läbi")
        return eeltekst
    rida, viimane_s6na = kirjuta_rida(v6tmes6na, eeltekst)
    eeltekst.append(rida)
    v6tmes6na = viimane_s6na.strip(".")
    tee_luuletus(v6tmes6na, eeltekst, loendur, ridu)
    return eeltekst



#MAIN
#algs6na = input("Algsõna: ")


luuletus = tee_luuletus("naine", ridu=30)
for line in luuletus:
    print(line)
