__author__ = 'ATM'
#in: list of douples with 3 els; ...... , ..... ,  ...key..., ....
def teeFraasideks(lause):
    fraasid = lause.split(", ")
    return fraasid

def vahetaFraasid(lause, v6tmes6na):
    print(lause, v6tmes6na)
    fraasid = teeFraasideks(lause)
    v6tmefraas = 0
    for fraas in fraasid:
        if v6tmes6na in fraas:
            v6tmefraas = fraas
    fraasid.remove(v6tmefraas)
    fraasid = [v6tmefraas]+fraasid
    lause = ", ".join(fraasid)
    return lause

def vahetaS6nad(fraas, v6tmes6na):
    s6nad = fraas.split(" ")
    for s6na in s6nad:
        if v6tmes6na in s6na:
            v6tmes6na = s6na
    s6nad.remove(v6tmes6na)
    s6nad = [v6tmes6na]+s6nad
    fraas = " ".join(s6nad)
    return fraas

def parafraseeri(lause, v6tmes6na):
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
    return v2ljund
