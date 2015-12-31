__author__ = 'Kaspar K2ngsepp'

from tkinter import *
from tkinter import ttk
from generaator import tee_luuletus
from uudiste_import import *

def kuva_luuletus(*args):
    #try:
    luuletus.set("LUULETUST GENEREERITAKSE...")
    root.update()
    s6na = str(võtmes6na.get())
    #KAALUD: võtmesõna indeks, vanasõna pikkus, juhuslikkus, leidub sõna esialgsel kujul (mitte lemma), vanas6na levik,
#       v6tmesõna suhteline asetus, võtmesõna täpsel kujul (mitte sõna osana), parafraseeritud
    kaalud=[asetus.get(),rea_pikkus.get(),juhuslikkus.get(),esialgsus.get(),levik.get(),asetus2.get(),t2psus.get(),parafraseeri.get(), koosneb_kahest_fraasist.get()]
    ridadelist = tee_luuletus(s6na, kaalud, tekst=[""], loendur=0, ridu=12, kasutatud=[])
    teksti_kujul = ""
    for element in ridadelist:
        teksti_kujul += element + "\n"
    luuletus.set(teksti_kujul)
    print(teksti_kujul)

def kuva_uudis_luuletus(*args):
    #try:
    luuletus.set("LUULETUST GENEREERITAKSE...")
    root.update()

    #KAALUD: võtmesõna indeks, vanasõna pikkus, juhuslikkus, leidub sõna esialgsel kujul (mitte lemma), vanas6na levik,
#       v6tmesõna suhteline asetus, võtmesõna täpsel kujul (mitte sõna osana), parafraseeritud
    kaalud=[asetus.get(),rea_pikkus.get(),juhuslikkus.get(),esialgsus.get(),levik.get(),asetus2.get(),t2psus.get(),parafraseeri.get(), koosneb_kahest_fraasist.get()]
    uudis = vali_uudis(puhasta(improdi_uudised()))
    s6nad = uudis2v6tmesõnad(uudis)
    ridadelist = tee_luuletus(s6nad, kaalud, tekst=[uudis], loendur=0, ridu=12, kasutatud=[])
    teksti_kujul = ""
    for element in ridadelist:
        teksti_kujul += element + "\n"
    luuletus.set(teksti_kujul)
    print(teksti_kujul)

root = Tk()
root.title("Luuletuse generaator")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

võtmes6na = StringVar()
luuletus = StringVar()

võtmes6na_entry = ttk.Entry(mainframe, width=20, textvariable=võtmes6na)
võtmes6na_entry.grid(column=2, row=1, sticky=(W, E))
#Sisendiväli, nupud
ttk.Label(mainframe, textvariable=luuletus).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Kirjuta", command=kuva_luuletus).grid(column=3, row=1, sticky=W)

ttk.Button(mainframe, text="Loe", command=kuva_uudis_luuletus).grid(column=2, row=2)
#Tekst
ttk.Label(mainframe, text="Sõna: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="M. Kohava").grid(column=1, row=13, sticky=W)
ttk.Label(mainframe, text="K. Kängsepp").grid(column=3, row=13, sticky=W)
#Pildid
image1 = PhotoImage(file='kk1.png')
image2 = PhotoImage(file='kk2.png')
ttk.Label(mainframe, image = image1).grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, image = image2).grid(column=3, row=3, sticky=E)

#Slaiderid
ttk.Label(mainframe, text="SAATUS").grid(column=1, row=4, sticky=E)
juhuslikkus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0.0, to=0.5)
juhuslikkus.grid(column=2, row=4)
juhuslikkus.set(0.2)

ttk.Label(mainframe, text="TÕDE").grid(column=1, row=5, sticky=E)
rea_pikkus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-1, to=-0.1)
rea_pikkus.grid(column=2, row=5)
rea_pikkus.set(-0.7)

ttk.Label(mainframe, text="TÖÖ").grid(column=1, row=6, sticky=E)
asetus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-0.4, to=-0.7)
asetus.grid(column=2, row=6)
asetus.set(-0.5)

ttk.Label(mainframe, text="VERI").grid(column=1, row=7, sticky=E)
asetus2 = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-0.4, to=-0.7)
asetus2.grid(column=2, row=7)
asetus2.set(-0.5)

ttk.Label(mainframe, text="ARMASTUS").grid(column=1, row=8, sticky=E)
esialgsus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0.1, to=0.7)
esialgsus.grid(column=2, row=8)
esialgsus.set(0.2)

ttk.Label(mainframe, text="AU").grid(column=1, row=9, sticky=E)
levik = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0, to=1.0)
levik.grid(column=2, row=9)
levik.set(0)

ttk.Label(mainframe, text="ÕIGUS").grid(column=1, row=10, sticky=E)
t2psus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0.1, to=0.7)
t2psus.grid(column=2, row=10)
t2psus.set(0.2)

ttk.Label(mainframe, text="JÄÄ").grid(column=1, row=11, sticky=E)
parafraseeri = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-1, to=0.5)
parafraseeri.grid(column=2, row=11)
parafraseeri.set(-0.2)

ttk.Label(mainframe, text="TULI").grid(column=1, row=12, sticky=E)
koosneb_kahest_fraasist = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0, to=1)
koosneb_kahest_fraasist.grid(column=2, row=12)
koosneb_kahest_fraasist.set(0.3)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

võtmes6na_entry.focus()
root.bind('<Return>', kuva_luuletus)

root.mainloop()