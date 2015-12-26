__author__ = 'ATM'
from itertools import *

def teeFraasideks(lause):
    fraasid = lause.split(", ")
    return fraasid

def permuteeriFraas(fraas):
    #võib asendada parema toekniseerimisega
    s6nad = fraas.split(" ")
    permutatsioonid = list(permutations(s6nad))
    parafraasid = []
    for permutatsioon in permutatsioonid:
        print(permutatsioon)
        parafraasid.append(" ".join(permutatsioon))
    return parafraasid

def permuteeriLause(lause):
    fraasid = teeFraasideks(lause)
    permutatsioonid = list(permutations(fraasid))
    paralaused = []
    for permutatsioon in permutatsioonid:
        paralaused.append(", ".join(permutatsioon))
    #print(paralaused)
    return paralaused

#permuteeriLause("Unusta uni, mäleta mälu, pea noor mees meeles")
###MAIN
#Siend: [(id, vanasõna, levik)...]
#Väljund: [(id, vanasõna, levik)...]

def parafraseeriLaused(sisendid):
    paralaused = []
    for sisend in sisendid:
        id, lause, levik = sisend
        permutatsioonid = list(lause for lause in permuteeriLause(lause))
        for permutatsioon in permutatsioonid:
            paralaused.append((id, permutatsioon, levik))
    return paralaused

def parafraseeriEsimesedJaViimasedFraasid(sisendid):
    paralaused = []
    for sisend in sisendid:
        id, lause, levik = sisend
        fraasid = teeFraasideks(lause)
        esimesePermutatsioonid = permuteeriFraas(fraasid[0])
        if len(fraasid)!= 1:
            viimasePermutatsioonid = permuteeriFraas(fraasid[-1])
            for permutatsioon1 in esimesePermutatsioonid:
                for permutatsioon2 in viimasePermutatsioonid:
                    if len(fraasid) != 2:
                        paralause = permutatsioon1+", "+(", ".join(fraasid[1:-1]))+", "+permutatsioon2
                        paralaused.append((id,paralause,levik))
                    else:
                        paralause= permutatsioon1+", "+permutatsioon2
                        paralaused.append((id,paralause,levik))
        else:
            for permutatsioon1 in esimesePermutatsioonid:
                paralause = permutatsioon1
                paralaused.append((id,paralause,levik))
    return paralaused

def parafraseeriEsimesedFraasid(sisendid):
    paralaused = []
    for sisend in sisendid:
        id, lause, levik = sisend
        fraasid = teeFraasideks(lause)
        esimesePermutatsioonid = permuteeriFraas(fraasid[0])
        if len(fraasid)!= 1:
            for permutatsioon1 in esimesePermutatsioonid:
                paralause = permutatsioon1+", "+(", ".join(fraasid[1:-1]))
                paralaused.append((id,paralause,levik))
        else:
            for permutatsioon1 in esimesePermutatsioonid:
                paralause = permutatsioon1
                paralaused.append((id,paralause,levik))
    print(paralaused)
    return paralaused

#parafraseeriLaused([(1, "Tuleb aeg, tuleb uus, tuleb parem", 3)])
#permuteeriFraas("Ei aeg meest oota")
#print(parafraseeriEsimesedJaViimasedFraasid([(1, "Tuleb aeg, tuleb uus, tuleb parem, tuleb targem", 3)]))

