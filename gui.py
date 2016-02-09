__author__ = 'Kaspar Kängsepp'
import webbrowser
from tkinter import *
from tkinter import ttk
from generaator import tee_luuletus
from uudiste_import import *

def l6ikelauale():
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    pk = pealkiri.get()
    if pk != '':
        pk += '\n'
    r.clipboard_append(pk + luuletus.get())
    r.destroy()

def kuva_luuletus(*args):
    try:
        requests.get('http://www.folklore.ee/')
        pealkiri.set("")
        luuletus.set("LUULETUST GENEREERITAKSE...")
        root.update()
        s6na = str(võtmes6na.get())
        # KAALUD: võtmesõna indeks, vanasõna pikkus, juhuslikkus, leidub sõna esialgsel kujul (mitte lemma),
        # vanas6na levik, v6tmesõna suhteline asetus, võtmesõna täpsel kujul (mitte sõna osana), parafraseeritud
        kaalud = [asetus.get(), rea_pikkus.get(), juhuslikkus.get(), esialgsus.get(), levik.get(), asetus2.get(), t2psus.get(), parafraseeri.get(), koosneb_kahest_fraasist.get()]
        ridu = int(realiugur.get())
        ridadelist = tee_luuletus(s6na, kaalud, ridu, tekst=[""], loendur=0, kasutatud=[])
        # pealkiri.set(s6na)
        linkTekstina.set("www.github.com/mohava/metaluule")
        teksti_kujul = ""
        for element in ridadelist:
            teksti_kujul += element + "\n"
        luuletus.set(teksti_kujul)
        # print(teksti_kujul)
    except:
        luuletus.set("KONTROLLIGE \nINTERNETIÜHENDUST")
        root.update()

def kuva_uudis(event):
    link = linkTekstina.get()
    webbrowser.open_new(link)

def kuva_uudis_luuletus(*args):
    try:
        requests.get('http://www.folklore.ee/')
        pealkiri.set("")
        luuletus.set("LUULETUST GENEREERITAKSE...")
        root.update()

        # KAALUD: võtmesõna indeks, vanasõna pikkus, juhuslikkus, leidub sõna esialgsel kujul (mitte lemma), vanas6na levik,
        # v6tmesõna suhteline asetus, võtmesõna täpsel kujul (mitte sõna osana), parafraseeritud
        kaalud = [asetus.get(), rea_pikkus.get(), juhuslikkus.get(), esialgsus.get(), levik.get(), asetus2.get(), t2psus.get(), parafraseeri.get(), koosneb_kahest_fraasist.get()]
        uudis, uudiselink = vali_uudis(puhasta(improdi_uudised()))
        s6nad = uudis2v6tmesõnad(uudis)
        ridu = int(realiugur.get())
        ridadelist = tee_luuletus(s6nad, kaalud, ridu, tekst=[uudis], loendur=0, kasutatud=[])

        pealkiri.set(ridadelist[0])
        linkTekstina.set(uudiselink)

        teksti_kujul = ""
        for element in ridadelist[1:]:
            teksti_kujul += element + "\n"
        luuletus.set(teksti_kujul)
        # print(teksti_kujul)
    except:
        luuletus.set("KONTROLLIGE \nINTERNETIÜHENDUST")
        root.update()


legendkuvatud = False

def vaheta_legend():
    global legendkuvatud
    if not legendkuvatud:
        leg1.set('Juhuslikkus'), leg2.set('Rea pikkus'), leg3.set('Võtmesõna asetus'), leg4.set('Suhteline asetus'), leg5.set('Esialgsus')
        leg6.set('Populaarsus'), leg7.set('Eraldiseisvus'), leg8.set('Parafraseerimine'), leg9.set('Mitmefraasilisus')
        legendkuvatud = True
    else:
        leg1.set('SAATUS'), leg2.set('TÕDE'), leg3.set('TÖÖ'), leg4.set('VERI'), leg5.set('ARMASTUS')
        leg6.set('AU'), leg7.set('ÕIGUS'), leg8.set('JÄÄ'), leg9.set('TULI')
        legendkuvatud = False


root = Tk()
root.title("Vanavärsside põimija")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

võtmes6na = StringVar()
luuletus = StringVar()
pealkiri = StringVar()
linkTekstina = StringVar()


võtmes6na_entry = ttk.Entry(mainframe, width=20, textvariable=võtmes6na)
võtmes6na_entry.grid(column=2, row=1, sticky=(W, E))
# Sisendiväli, nupud, väljund
pealkiriObjekt = ttk.Label(mainframe, textvariable=pealkiri)
pealkiriObjekt.grid(column=2, row=2, sticky=(W, E))
pealkiriObjekt.bind("<Button-1>", kuva_uudis)

luuletusObjekt = ttk.Label(mainframe, textvariable=luuletus)
luuletusObjekt.grid(column=2, row=3, sticky=(W, N, E))
luuletusObjekt.bind("<Button-1>", kuva_uudis)
ttk.Button(mainframe, text="Kirjuta", command=kuva_luuletus).grid(column=3, row=1, sticky=W)

ttk.Button(mainframe, text="Kopeeri", command=l6ikelauale).grid(column=3, row=12)

ttk.Button(mainframe, text="Loe lehest", command=kuva_uudis_luuletus).grid(column=2, row=13)
# Tekst
ttk.Label(mainframe, text="Sõna: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="M. Kohava").grid(column=1, row=13, sticky=W)
ttk.Label(mainframe, text="K. Kängsepp").grid(column=3, row=13, sticky=W)
# Pildid
image1 = PhotoImage(file='kk1.png')
image2 = PhotoImage(file='kk2.png')
ttk.Label(mainframe, image=image1).grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, image=image2).grid(column=3, row=3, sticky=E)

# Spinbox
ttk.Label(mainframe, text='Vanasõnu:').grid(column=3, row=5, sticky=E)
ridu = StringVar()
ridu.set('12')
realiugur = Spinbox(mainframe, from_=4, to=20, textvariable=ridu, width=6)
realiugur.grid(column=3, row=6, sticky=E)

# LEGENDI KUVA
ttk.Button(mainframe, text="Legend", command=vaheta_legend).grid(column=3, row=7, )  # sticky=W)
leg1, leg2, leg3, leg4, leg5 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
leg6, leg7, leg8, leg9 = StringVar(), StringVar(), StringVar(), StringVar()
leg1.set('SAATUS'), leg2.set('TÕDE'), leg3.set('TÖÖ'), leg4.set('VERI'), leg5.set('ARMASTUS')
leg6.set('AU'), leg7.set('ÕIGUS'), leg8.set('JÄÄ'), leg9.set('TULI')

# Slaiderid
ttk.Label(mainframe, textvariable=leg1).grid(column=1, row=4, sticky=E)
juhuslikkus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0.0, to=0.5)
juhuslikkus.grid(column=2, row=4)
juhuslikkus.set(0.3)

ttk.Label(mainframe, textvariable=leg2).grid(column=1, row=5, sticky=E)
rea_pikkus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-1, to=-0.1)
rea_pikkus.grid(column=2, row=5)
rea_pikkus.set(-0.8)

ttk.Label(mainframe, textvariable=leg3).grid(column=1, row=6, sticky=E)
asetus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-0.3, to=-0.8)
asetus.grid(column=2, row=6)
asetus.set(-0.5)

ttk.Label(mainframe, textvariable=leg4).grid(column=1, row=7, sticky=E)
asetus2 = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-0.3, to=-0.8)
asetus2.grid(column=2, row=7)
asetus2.set(-0.5)

ttk.Label(mainframe, textvariable=leg5).grid(column=1, row=8, sticky=E)
esialgsus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0.1, to=0.7)
esialgsus.grid(column=2, row=8)
esialgsus.set(0.4)

ttk.Label(mainframe, textvariable=leg6).grid(column=1, row=9, sticky=E)
levik = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0, to=1.0)
levik.grid(column=2, row=9)
levik.set(0.2)

ttk.Label(mainframe, textvariable=leg7).grid(column=1, row=10, sticky=E)
t2psus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0.1, to=0.7)
t2psus.grid(column=2, row=10)
t2psus.set(0.4)

ttk.Label(mainframe, textvariable=leg8).grid(column=1, row=11, sticky=E)
parafraseeri = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-1, to=0.5)
parafraseeri.grid(column=2, row=11)
parafraseeri.set(-0.2)

ttk.Label(mainframe, textvariable=leg9).grid(column=1, row=12, sticky=E)
koosneb_kahest_fraasist = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0, to=1)
koosneb_kahest_fraasist.grid(column=2, row=12)
koosneb_kahest_fraasist.set(0.2)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

võtmes6na_entry.focus()
root.bind('<Return>', kuva_luuletus)

root.mainloop()
