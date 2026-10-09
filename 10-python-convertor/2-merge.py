# Convertor de unitati - varianta 2
# Rulare: python 2-merge.py  (pe Windows: py 2-merge.py)
import tkinter as tk
from tkinter import messagebox

NIVEL = ("Nivelul 2 din 4 – Merge (works)",
         "Aplicația își face treaba, dar este neintuitivă, inconsecventă sau nu se adaptează "
         "la ecrane mici.")

# fiecare unitate: (categorie, factor, decalaj); valoare_baza = valoare * factor + decalaj
UNITATI = {
    "m": ("L", 1, 0), "km": ("L", 1000, 0), "cm": ("L", 0.01, 0), "ft": ("L", 0.3048, 0),
    "mi": ("L", 1609.344, 0), "kg": ("M", 1, 0), "g": ("M", 0.001, 0),
    "lb": ("M", 0.45359237, 0), "C": ("T", 1, 0), "F": ("T", 5 / 9, -160 / 9),
    "K": ("T", 1, -273.15),
}


def converteste():
    try:
        x = float(e_valoare.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
        return
    cat1, f1, d1 = UNITATI[din.get()]
    cat2, f2, d2 = UNITATI[spre.get()]
    if cat1 != cat2:
        messagebox.showerror("Error", "Error 42: incompatible units")
        return
    baza = x * f1 + d1
    lbl_rezultat.config(text="Result: %.2f" % ((baza - d2) / f2))


def arata_nivel():
    messagebox.showinfo("Ce nivel are interfața?", NIVEL[0] + "\n\n" + NIVEL[1] +
                        "\n\nComparați cu celelalte variante și cu fișa de lucru (FISA.md).")


root = tk.Tk()
root.title("Unit Converter")
root.geometry("340x200")
root.resizable(False, False)

tk.Label(root, text="Valoare").place(x=10, y=12)
e_valoare = tk.Entry(root, width=12)
e_valoare.place(x=70, y=12)

tk.Label(root, text="From:").place(x=10, y=50)
din = tk.StringVar(value="m")
tk.OptionMenu(root, din, *UNITATI).place(x=55, y=45)
tk.Label(root, text="in").place(x=130, y=50)
spre = tk.StringVar(value="m")
tk.OptionMenu(root, spre, *UNITATI).place(x=150, y=45)

tk.Button(root, text="Convert", command=converteste).place(x=230, y=45)
lbl_rezultat = tk.Label(root, text="Result:", font=("Arial", 12))
lbl_rezultat.place(x=10, y=100)

tk.Button(root, text="Ce nivel are interfața?", font=("Arial", 8), relief="flat", fg="#555555",
          command=arata_nivel).place(relx=1.0, rely=1.0, x=-4, y=-4, anchor="se")

root.mainloop()
