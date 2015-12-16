from tkinter import *
from tkinter import ttk
from generaator import tee_luuletus



def kuva_luuletus(*args):

    try:
        luuletus.set("LUULETUST GENEREERITAKSE...")
        root.update()
        s6na = str(vıtmes6na.get())
        teksti_kujul = ""
        #print(juhuslikkus.get()) #ma ei saa v‰‰rtust k‰tte slaideritest
        #print(rea_pikkus.get())
        kaalud = [-0.5,-0.2, juhuslikkus.get(), 1, 0.2, -0.5, 0.1]
        print(kaalud)
        ridadelist = tee_luuletus(s6na, kaalud=kaalud)
        for element in ridadelist:
            teksti_kujul += element + "\n"
        luuletus.set(teksti_kujul)
    except:
        print("Viga gui.py-s")

root = Tk()
root.title("Luuletuse generaator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

vıtmes6na = StringVar()
luuletus = StringVar()

vıtmes6na_entry = ttk.Entry(mainframe, width=20, textvariable=vıtmes6na)
vıtmes6na_entry.grid(column=2, row=1, sticky=(W, E))
#Sisendiv‰li, nupp
ttk.Label(mainframe, textvariable=luuletus).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Genereeri", command=kuva_luuletus).grid(column=3, row=1, sticky=W)
#Tekst
ttk.Label(mainframe, text="Vıtmesına: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="M. Kohava").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="K. K‰ngsepp").grid(column=3, row=5, sticky=W)
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
rea_pikkus = ttk.Scale(mainframe, orient=HORIZONTAL, length=100, from_=-1, to=-0.1).grid(column=2, row=4)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

vıtmes6na_entry.focus()
root.bind('<Return>', kuva_luuletus)

root.mainloop()