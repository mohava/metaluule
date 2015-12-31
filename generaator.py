__author__ = 'Mihkel'
from vanas6nade_import import kysi_vanas6nad
from collections import defaultdict
from random import randint
from lemmatiseerija import lemmatiseeri
from lyhendaja import lyhenda
from parafraseerija import parafraseeriLaused
from syntesaator import synteseeri
from copy import deepcopy
from ridade_asetus import  ilusta

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

        ##BUG##
        #print("võtmed",v6tmes6nad)
        #print("SÕNA",s6na)
        #print(v6tmes6na,"!!!!", vanas6na)
        try:
            s6na_asetus = vanas6na.index(v6tmes6na)
        except:
            print("VIGA")
            s6na_asetus = 0

        v6tmes6na_t2pselt_kujul = (" "+v6tmes6na+" ") in vanas6na
        vanas6na_pikkus = len(vanas6na)
        koosneb_kahest_fraasist = (len(vanas6na.split(", ")) == 2)

        parameetrid[vanas6na] = [s6na_asetus, vanas6na_pikkus, originaals6na, levik, v6tmes6na_t2pselt_kujul, parafraseeritud, koosneb_kahest_fraasist, idNumber]
    return parameetrid

#kood on kirjutatud pidades silmas, et siina vahel saaks olla kaalude optimeerimise funktsioon
#kaalud = kaalud()

#KAALUD: võtmesõna indeks, vanasõna pikkus, juhuslikkus, leidub sõna esialgsel kujul (mitte lemma), vanas6na levik,
#       v6tmesõna suhteline asetus, võtmesõna täpsel kujul (mitte sõna osana), parafraseeritud, koosneb kahest fraasist
def leia_parim_vanas6na(parameetrid, kasutatud, kaalud=[-0.5,-0.7, 0.5, 0.2, 0.5, -0.5, 0.2, -0.5, 0.5]):
    #print("tik-tok")
    skoorid = []
    for vanas6na in parameetrid:
        s6na_indeks, vanas6na_pikkus, originaals6na, levik, v6tmes6na_t2psel_kujul, parfraseeritud, \
                koosneb_kahest_fraasist, idNumber = parameetrid[vanas6na]

        skoor = s6na_indeks*kaalud[0] + vanas6na_pikkus*kaalud[1] + randint(0,100)*kaalud[2] \
                    + originaals6na*100*kaalud[3] + levik*kaalud[4] + s6na_indeks/vanas6na_pikkus*100*kaalud[5] \
                    + v6tmes6na_t2psel_kujul*100*kaalud[6] + parfraseeritud*kaalud[7]*100 \
                    + koosneb_kahest_fraasist*100*kaalud[8]

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
        print("lemmatiseerin-sünteerin")
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
    print("RIDA", rida)
    return rida, viimane_s6na, kasutatud

def abifunktsioon(v6tmes6nad, kaalud, kasutatud):
    for v6tmes6na in v6tmes6nad:
        #v6tmes6na = v6tmes6na.lower()
        #print("click-click", v6tmes6na)
        rida, viimane_s6na, kasutatud = kirjuta_rida(v6tmes6na, kaalud, kasutatud)
        if rida != "luuletus sai läbi":
            return rida, viimane_s6na, kasutatud
    else:
        return "luuletus sai läbi", "", []

def tee_luuletus(v6tmes6nad, kaalud=[-0.5,-0.7, 0.5, 0.2, 0.5, -0.5, 0.2, -0.5, 0.5], ridu=12, tekst=[""], loendur=0, kasutatud=[]):
    #v6tmes6na = v6tmes6na.lower()
    loendur +=1
    if loendur == ridu:
        return ilusta(tekst)
    if tekst[-1] == "luuletus sai läbi":
        tekst = tekst.remove("luuletus sai läbi")
        return tekst
    if type(v6tmes6nad) != list:
        v6tmes6nad = [v6tmes6nad]
    #print("enne abifunci", v6tmes6nad)
    rida, viimane_s6na, kasutatud = abifunktsioon(v6tmes6nad, kaalud, kasutatud)

    #print(rida)
    #print(tekst)
    tekst.append(rida)
    v6tmes6na = viimane_s6na.strip(".")
    tee_luuletus(v6tmes6na, kaalud, ridu, tekst, loendur, kasutatud)
    return ilusta(tekst)



#TEHA: mitmeharuline rekursioon (kogu luuletuse skoori arvutamine), parima luuletuse esitamine  8/10= 0.8
#TEHA: kui ei leia viimast sõna siis lisada rida "viimane sõna, sünonüüm"  4/5
#TEHA: kui ei leia viimast sõna siis lisada rida "viimane sõna, riimuv sõna" kus riimuv sõna on sama lõpu ja silpide arvuga 4/5
#TEHA: salvestada päringute tulemused anmbaasi: päritud võtmesõnad ja vanasõnad 2/10
#THEA: normaliseerida  iga seti skoorid 9/8
#TEHA: features: riimub? sama pikkus mis eelmisel? 4/8
#TEHA: feat: kahest fraasist koosnev 9/6
#TEHA: parafraseerija: ei kõige esimeseks 5/5
#TEHA: kaks eraldi parafraseerimsit 9/10
#TEHA: GUIsse ridade arv 6/3 EI
#TEHA: GUIsse poliitika 6/4
#TEHA: pikad read paremini vormistada
#TEHA: siluda ja ühtlustada generaatori koodi

###MAIN###

"""
luuletus = tee_luuletus("kolm",kaalud=[-0.5,-0.7, 0, 0.2, 0.5, -0.5, 0.2, -0.5, 0.5], tekst=[""], loendur=0, ridu=12, kasutatud=[])
for line in luuletus:
    print(line)
"""