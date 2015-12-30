__author__ = 'Mihkel Kohava'
def teeFraasideks(lause):
    fraasid = lause.split(", ")
    return fraasid

def vahetaFraasid(lause, v6tmes6nad):
    #print(lause, v6tmes6na)
    #print(v6tmes6nad, lause)
    fraasid = teeFraasideks(lause)
    #v6tmes6nad = set(v6tmes6nad)
    #print(v6tmes6nad)
    v6tmefraas = "Viga parafraseerimises"
    for fraas in fraasid:
        for v6tmes6na in v6tmes6nad:
            if v6tmes6na in fraas:
                v6tmefraas = fraas
    if v6tmefraas in fraasid:
        fraasid.remove(v6tmefraas)
    else:
        print("jätsin parafraseerimata")
        print("Fraasid:", fraasid)
        print("Võtmefraas: ", v6tmefraas)
        return lause
    fraasid = [v6tmefraas]+fraasid
    lause = ", ".join(fraasid)
    return lause

def vahetaS6nad(fraas, v6tmes6nad):
    s6nad = fraas.split(" ")
    valitudS6na = "Viga vahetaS6nades"
    for s6na in s6nad:
        for v6tmes6na in v6tmes6nad:
            if v6tmes6na in s6na:
                valitudS6na = s6na
    if valitudS6na in s6nad:
        s6nad.remove(valitudS6na)
    else:
        print("jätsin parafraseerimata")
        print("Parafraseerimine: Fraas:", fraas)
        print("Parafraseerimine: Valitud sõna:", valitudS6na)
        print("Parafraseermine: võtmesõna:", v6tmes6na)
        return fraas
    s6nad = [valitudS6na]+s6nad
    fraas = " ".join(s6nad)
    #print(fraas)
    return fraas

def parafraseeri(lause, v6tmes6na):
    if type(v6tmes6na) != set:
        v6tmes6na = {v6tmes6na}
    lause = lause.lower()
    lause = vahetaFraasid(lause, v6tmes6na)
    fraasid = lause.split(", ")
    esimeneFraas = fraasid.pop(0)
    esimeneFraas = vahetaS6nad(esimeneFraas, v6tmes6na)
    lause = [esimeneFraas] + fraasid
    lause = ", ".join(lause)
    return lause

def parafraseeriLaused(sisendid, v6tmes6na):
    v2ljund = []
    for sisend in sisendid:
        id, lause, levik = sisend
        lause = parafraseeri(lause, v6tmes6na)
        v2ljund.append((id, lause, levik))
    #print("parafraseeritud", v2ljund)
    return v2ljund