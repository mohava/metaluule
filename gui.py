from tkinter import *
from tkinter import ttk
from generaator import tee_luuletus
def kuva_luuletus(*args):
    #try:
    luuletus.set("LUULETUST GENEREERITAKSE...")
    root.update()
    s6na = str(võtmes6na.get())
    kaalud=[round(asetus.get(),1),round(juhuslikkus.get(),1),round(rea_pikkus.get(),1),0.5,0.5,0.5,0.5]
    #kui slaidereid ei liiguta, siis nende väärtuseks 0 !!!
    ridadelist = tee_luuletus(s6na, kaalud, eeltekst=[""], loendur=0, ridu=12)
    teksti_kujul = ""
    for element in ridadelist:
        teksti_kujul += element + "\n"
    luuletus.set(teksti_kujul)
    #except:
    #    print("Viga gui.py-s")
root = Tk()
root.title("Luuletuse generaator")
a
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

võtmes6na = StringVar()
luuletus = StringVar()

võtmes6na_entry = ttk.Entry(mainframe, width=20, textvariable=võtmes6na)
võtmes6na_entry.grid(column=2, row=1, sticky=(W, E))
#Sisendiväli, nupp
ttk.Label(mainframe, textvariable=luuletus).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Genereeri", command=kuva_luuletus).grid(column=3, row=1, sticky=W)
#Tekst
ttk.Label(mainframe, text="Võtmesõna: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="M. Kohava").grid(column=1, row=10, sticky=W)
ttk.Label(mainframe, text="K. Kängsepp").grid(column=3, row=10, sticky=W)
#Pildid
image1 = PhotoImage(file='kk1.png')
image2 = PhotoImage(file='kk2.png')
ttk.Label(mainframe, image = image1).grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, image = image2).grid(column=3, row=2, sticky=E)

#Slaiderid
ttk.Label(mainframe, text="Juhuslikkus").grid(column=1, row=3, sticky=E)
juhuslikkus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=0, to=0.5)
juhuslikkus.grid(column=2, row=3)

ttk.Label(mainframe, text="Rea pikkus").grid(column=1, row=4, sticky=E)
rea_pikkus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-1, to=0.1)
rea_pikkus.grid(column=2, row=4, sticky=W)

ttk.Label(mainframe, text="Võtmesõna asetus").grid(column=1, row=5, sticky=E)
asetus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-0.4, to=-0.7)
asetus.grid(column=2, row=5, sticky=W)

'''#spinbox
rea_pikkus = StringVar()
rea_pikkus = Spinbox(mainframe, from_=-1, to=0.1, textvariable=rea_pikkus,increment=0.1)
rea_pikkus.grid(column=2, row=4, sticky=W)
'''
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

võtmes6na_entry.focus()
root.bind('<Return>', kuva_luuletus)

root.mainloop()