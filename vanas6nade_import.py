import requests
from bs4 import BeautifulSoup
'''#defineeri siia funktisoon, mis võtab sisendiks sõna ja tagastab listi,
#  kus on kõik päringust saadud vanasõnad (iga vanasõna on listi üks element)
#def kysi_vanas6nad(sõna):'''


#r = requests.get('http://www.folklore.ee/rl/date/robotid/leht1.html')
#print(r.content)

'''soup = BeautifulSoup(r.content)
tag = soup.b
print(tag)'''
#r = requests.options('http://www.folklore.ee/rl/date/robotid/leht1.html')
r = requests.post('http://www.folklore.ee/rl/date/robotid/leht1.html', data = {"/html/body/center/table[2]/tbody/tr[1]/td[1]/form/inFUCKFUCKFUCKput[1]":"mees"}) ####response 200
print(r.text.encode("utf-8"))