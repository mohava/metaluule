__author__ = 'ATM'
from vanas6nade_import import kysi_vanas6nad
from collections import defaultdict

#küsi kasutajalt input
#tee luuletus:
 #tee esimene rida
#

#parameetrid: sõna asetus, vanasõna pikkus
def leia_vanas6nade_parameetrid(v6tmes6na, uued_vanas6nad):
    parameetrid=defaultdict(list)
    #print(v6tmes6na)
    for idNumber, vanas6na, levik in uued_vanas6nad:
        #print(vanas6na)
        vanas6na = vanas6na.lower()
        s6na_asetus = vanas6na.index(v6tmes6na)
        vanas6na_pikkus = len(vanas6na)
        parameetrid[vanas6na] = [s6na_asetus, vanas6na_pikkus]
    return parameetrid

#kood on kirjutatud pidades silmas, et siina vahel saaks olla kaalude optimeerimise funktsioon

def leia_parim_vanas6na(parameetrid, eeltekst, kaalud=[-1,-1]):
    skoorid = []
    #print(eeltekst)
    for vanas6na in parameetrid:
        s6na_indeks, vanas6na_pikkus = parameetrid[vanas6na]
        skoor = s6na_indeks*kaalud[0] + vanas6na_pikkus*kaalud[1]
        #print(vanas6na)
        #print(skoor, ":", s6na_indeks , vanas6na_pikkus)
        skoorid.append((skoor, vanas6na))
    skoorid = sorted(skoorid, reverse=1)
    i = 0
    for skoor,parim_vanas6na in skoorid:
        i += 1
        if parim_vanas6na not in eeltekst:
            print("jah")
            return parim_vanas6na
        if i == len(skoorid):
            return ("Luuletus sai läbi")
    #print(skoorid)
    return parim_vanas6na

def kirjuta_rida(v6tmes6na, eeltekst):
    print("võtmesõna: ",v6tmes6na)
    vans6nad = kysi_vanas6nad(v6tmes6na)
    #print("vanasõnad:", vans6nad)
    parameetrid = leia_vanas6nade_parameetrid(v6tmes6na, vans6nad)
    #print("params:", parameetrid)
    rida = leia_parim_vanas6na(parameetrid, eeltekst)
    print("parim", rida)
    print()
    s6nad = rida.split()
    viimane_s6na = s6nad[-1]
    return rida, viimane_s6na

def tee_luuletus(v6tmes6na, eeltekst=[], loendur=0):
    loendur +=1
    """if loendur == 10:
        return eeltekst
    rida, viimane_s6na = kirjuta_rida(v6tmes6na, eeltekst)
    eeltekst.append(rida)
    v6tmes6na = viimane_s6na
    tee_luuletus(v6tmes6na, eeltekst, loendur)"""

    try:
        rida, viimane_s6na = kirjuta_rida(v6tmes6na, eeltekst)
        #print(viimane_s6na)
        #print(rida)
        #print(viimane_s6na)
        eeltekst.append(rida)
        v6tmes6na = viimane_s6na
        #print(rida)
        #print(viimane_s6na)
        tee_luuletus(v6tmes6na, eeltekst, loendur)
    except:
        return eeltekst
    return eeltekst



#MAIN
#algs6na = input("Algsõna: ")

luuletus = tee_luuletus("ilus")
for line in luuletus:
    print(line)

#rida, viimane_s6na = kirjuta_rida("mesdfkjd")
#print(rida)


