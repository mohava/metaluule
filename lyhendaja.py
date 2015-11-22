__author__ = 'Mihkel'

def lyhenda(vanas6na):
    s6nad = vanas6na.strip().split()
    kustutuatavad_s6nad = {"kus", "on", "oli", "kes"}
    uus_vanas6na = []
    for s6na in s6nad:
        if s6na not in kustutuatavad_s6nad:
            uus_vanas6na.append(s6na)
    uus_vanas6na = " ".join(uus_vanas6na)
    return uus_vanas6na