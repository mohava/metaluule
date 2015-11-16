import requests
from bs4 import BeautifulSoup
def kysi_vanas6nad(sona):
    r = requests.post('http://www.folklore.ee/cgi-bin/script1', data = {"entry":sona.encode("iso-8859-1")})
    #print(r.content) # selline html-kood on r.content -is

    soup = BeautifulSoup(r.content, "html.parser", )
    #print(soup.body.table.get_text())
    try:
        vanasonad = soup.body.table.get_text()
    except:
        print("Päringule ei vasta vanasõnu.")
        return None #seda rida vist ei ole siia vaja?
    list = []
    a,b,c = '','','' #kus a on vanasõna id, b on vanasõna, c on autentsete tekstide arv
    olinumber=False
    joutudvanasonani=False

    for element in vanasonad:
        if element == '\n' and joutudvanasonani == True:
            list.append((int(a),b,int(c)))
            a,b,c = '','',''
            olinumber=False
            joutudvanasonani=False
        elif element == '\r': # et vanasõna hulka ei tuleks sellist sümbolit
            1
        else:
            if element.isdigit():
                olinumber=True
                if joutudvanasonani:
                    c+=element
                else:
                    a+=element
            else:
                if olinumber:
                    joutudvanasonani=True
                    b+=element
    return list
#print(kysi_vanas6nad('õde'))