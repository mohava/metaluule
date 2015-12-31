__author__ = 'Mihkel Kohava'

import re

def ilusta(ridade_list):
    uus = []
    for rida in ridade_list:
        if len(rida) > 46 and any(el in rida for el in {",",";",":","-","/"}):
            #print(rida)
            fraasid = re.split(",|;|:|-|/", rida)
            #print(fraasid)
            fraasid = list(fraas.strip() for fraas in fraasid)
            uus.append(fraasid[0])
            if len(fraasid)>1:
                for fraas in fraasid[1:]:
                    uus.append("    "+fraas)

        elif len(rida) > 46:
            s6nad = rida.split(" ")
            fraasid = [' '.join(s6nad[:5]), ' '.join(s6nad[5:])]
            uus.append(fraasid[0])
            if len(fraasid)>1:
                for fraas in fraasid[1:]:
                    uus.append("    "+fraas)
        else:
            uus.append(rida)
    return uus

#print(ilusta(["proovinud kut uut pole veel läbi, ära unusta enne vanat soraj sdjfa"]))

#print(len("Eesti ülikoolid päästab ähvardavast rahahädast mõistlik tööjaotus"))