# Convertor de unitati - varianta 1
# Rulare: python 1-nu-merge.py  (pe Windows: py 1-nu-merge.py)
import tkinter as tk
from tkinter import messagebox

NIVEL = ("Nivelul 1 din 4 – Nu merge (doesn’t work)",
         "Sarcina se realizează greu sau deloc: lipsesc mesajele, butoanele nu sunt clare, "
         "erorile nu sunt explicate.")

# conversiile disponibile: cod -> functie
CONVERSII = {
    "C-F": lambda x: x * 9 / 5 + 32,
    "km-mi": lambda x: x / 1.609344,
    "lb-kg": lambda x: x * 0.45359237,
    "F-C": lambda x: (x - 32) * 5 / 9,
    "m-ft": lambda x: x / 0.3048,
    "kg-lb": lambda x: x / 0.45359237,
    "C-K": lambda x: x + 273.15,
    "ft-m": lambda x: x * 0.3048,
    "g-oz": lambda x: x / 28.349523125,
    "mi-km": lambda x: x * 1.609344,
}


def calculeaza():
    try:
        x = float(valoare.get())
    except ValueError:
        return
    rezultat.config(text=str(CONVERSII[cod.get()](x)))


def sterge():
    valoare.delete(0, "end")
    rezultat.config(text="")


def arata_nivel():
    messagebox.showinfo("Ce nivel are interfața?", NIVEL[0] + "\n\n" + NIVEL[1] +
                        "\n\nComparați cu celelalte variante și cu fișa de lucru (FISA.md).")


root = tk.Tk()
root.title("Conv")
root.geometry("260x110")
root.resizable(False, False)
root.configure(bg="#f2f2f2")
mic = ("Arial", 8)

valoare = tk.Entry(root, width=10, font=mic)
valoare.place(x=8, y=10)
cod = tk.StringVar(value="C-F")
meniu = tk.OptionMenu(root, cod, *CONVERSII)
meniu.config(font=mic, padx=0, pady=0, highlightthickness=0)
meniu.place(x=80, y=7)
tk.Button(root, text="=", font=mic, padx=2, pady=0, command=calculeaza).place(x=150, y=8)
tk.Button(root, text="C", font=mic, padx=2, pady=0, command=sterge).place(x=170, y=8)

rezultat = tk.Label(root, text="", font=mic, fg="#c8c8c8", bg="#f2f2f2")
rezultat.place(x=8, y=45)

tk.Button(root, text="Ce nivel are interfața?", font=("Arial", 7), relief="flat", fg="#555555",
          bg="#f2f2f2", command=arata_nivel).place(relx=1.0, rely=1.0, x=-4, y=-4, anchor="se")

root.mainloop()
