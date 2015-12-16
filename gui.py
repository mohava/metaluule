from tkinter import *
from tkinter import ttk
from generaator import tee_luuletus
from time import sleep

def kuva_luuletus(*args):
    try:
        luuletus.set("LUULETUST GENEREERITAKSE...")
        root.update()
        s6na = str(võtmes6na.get())
        teksti_kujul = ""
        for element in tee_luuletus(s6na, eeltekst=[""], loendur=0, ridu=12):
            teksti_kujul += element + "\n"
        #print(teksti_kujul)
        luuletus.set(teksti_kujul)
    except:
        pass
root = Tk()
root.title("Luuletuse generaator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

võtmes6na = StringVar()
luuletus = StringVar()

võtmes6na_entry = ttk.Entry(mainframe, width=10, textvariable=võtmes6na)
võtmes6na_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=luuletus).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Genereeri", command=kuva_luuletus).grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, text="Võtmesõna: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Luuletus: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="M.K. \n K.K.").grid(column=3, row=2, sticky=(E,S))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

võtmes6na_entry.focus()
root.bind('<Return>', kuva_luuletus)

root.mainloop()