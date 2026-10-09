# Temporizator de pauze - varianta 1
# Rulare: python 1-nu-merge.py  (pe Windows: py 1-nu-merge.py)
import tkinter as tk
from tkinter import messagebox

VITEZA = 1  # 1 = timp real; 60 = un minut trece intr-o secunda (doar pentru test)

NIVEL = ("Nivelul 1 din 4 – Nu merge (doesn’t work)",
         "Sarcina se realizează greu sau deloc: lipsesc mesajele, butoanele nu sunt clare, "
         "erorile nu sunt explicate.")

secunde = 0
durata = 0
mod = 1


def tic():
    global secunde, mod
    if secunde > 0:
        secunde -= 1
    else:
        # schimbare de etapa: 1 = lucru, 2 = pauza (pauza fixa, 300 s)
        mod = 2 if mod == 1 else 1
        secunde = 300 if mod == 2 else durata
    afisaj.config(text=str(secunde))
    eticheta_mod.config(text="mod " + str(mod))
    root.after(max(1, 1000 // VITEZA), tic)


def porneste():
    global secunde, durata, mod
    try:
        durata = int(timp.get())
    except ValueError:
        return
    secunde = durata
    mod = 1
    tic()


def opreste():
    # inchide aplicatia
    root.destroy()


def arata_nivel():
    messagebox.showinfo("Ce nivel are interfața?", NIVEL[0] + "\n\n" + NIVEL[1] +
                        "\n\nComparați cu celelalte variante și cu fișa de lucru (FISA.md).")


root = tk.Tk()
root.title("Timer")
root.geometry("230x95")
root.resizable(False, False)
root.configure(bg="#d9d9d9")
mic = ("Arial", 7)

tk.Label(root, text="Timp", font=mic, bg="#d9d9d9").place(x=6, y=8)
timp = tk.Entry(root, width=6, font=mic)
timp.place(x=36, y=8)
tk.Button(root, text="▶", font=mic, padx=1, pady=0, command=porneste).place(x=86, y=5)
tk.Button(root, text="■", font=mic, padx=1, pady=0, command=opreste).place(x=106, y=5)

afisaj = tk.Label(root, text="0", font=("Arial", 9), fg="#b4b4b4", bg="#d9d9d9")
afisaj.place(x=6, y=34)
eticheta_mod = tk.Label(root, text="mod 1", font=mic, fg="#c4c4c4", bg="#d9d9d9")
eticheta_mod.place(x=6, y=56)

tk.Button(root, text="Ce nivel are interfața?", font=("Arial", 7), relief="flat", fg="#555555",
          bg="#d9d9d9", command=arata_nivel).place(relx=1.0, rely=1.0, x=-4, y=-4, anchor="se")

root.mainloop()
