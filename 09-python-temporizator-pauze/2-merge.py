# Temporizator de pauze - varianta 2
# Rulare: python 2-merge.py  (pe Windows: py 2-merge.py)
import tkinter as tk
from tkinter import messagebox

VITEZA = 1  # 1 = timp real; 60 = un minut trece intr-o secunda (doar pentru test)

NIVEL = ("Nivelul 2 din 4 – Merge (works)",
         "Aplicația își face treaba, dar este neintuitivă, inconsecventă sau nu se adaptează "
         "la ecrane mici.")

ramas = 0          # secunde ramase din etapa curenta
etapa = "LUCRU"
pe_pauza = False
job = None         # identificatorul apelului programat cu after()


def format_timp(s):
    return "%02d:%02d" % (s // 60, s % 60)


def citeste_durate():
    try:
        lucru = int(e_lucru.get())
        pauza = int(e_pauza.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
        return None
    if lucru <= 0 or pauza <= 0:
        messagebox.showerror("Error", "Error 42")
        return None
    return lucru, pauza


def start():
    global ramas, etapa, pe_pauza, job
    durate = citeste_durate()
    if durate is None:
        return
    if job:
        root.after_cancel(job)  # porneste mereu de la inceput
    etapa, pe_pauza = "LUCRU", False
    ramas = durate[0] * 60
    tic()


def tic():
    global ramas, etapa, job
    if not pe_pauza:
        ramas -= 1
        if ramas < 0:
            messagebox.showinfo("Info", "Time is up!")
            durate = citeste_durate() or (50, 5)
            etapa = "PAUZA" if etapa == "LUCRU" else "LUCRU"
            ramas = (durate[1] if etapa == "PAUZA" else durate[0]) * 60
    lbl_timp.config(text=format_timp(ramas))
    lbl_etapa.config(text=etapa)
    job = root.after(max(1, 1000 // VITEZA), tic)


def pauza():
    global pe_pauza
    pe_pauza = not pe_pauza


def reset():
    global ramas, job
    if job:
        root.after_cancel(job)
        job = None
    ramas = 0
    lbl_timp.config(text="00:00")


def arata_nivel():
    messagebox.showinfo("Ce nivel are interfața?", NIVEL[0] + "\n\n" + NIVEL[1] +
                        "\n\nComparați cu celelalte variante și cu fișa de lucru (FISA.md).")


root = tk.Tk()
root.title("Temporizator")
root.geometry("320x210")
root.resizable(False, False)

tk.Label(root, text="Work (min):").place(x=10, y=10)
e_lucru = tk.Entry(root, width=8)
e_lucru.place(x=95, y=10)
tk.Label(root, text="Pauza:").place(x=170, y=10)
e_pauza = tk.Entry(root, width=6)
e_pauza.place(x=220, y=10)

lbl_etapa = tk.Label(root, text="LUCRU", font=("Arial", 9))
lbl_etapa.place(x=10, y=45)
lbl_timp = tk.Label(root, text="00:00", font=("Arial", 26))
lbl_timp.place(x=10, y=62)

tk.Button(root, text="Start", width=7, command=start).place(x=10, y=125)
tk.Button(root, text="Reset", width=7, bg="#e04040", fg="white", command=reset).place(x=105, y=125)
tk.Button(root, text="Pauza", width=7, command=pauza).place(x=200, y=125)

tk.Button(root, text="Ce nivel are interfața?", font=("Arial", 8), relief="flat", fg="#555555",
          command=arata_nivel).place(relx=1.0, rely=1.0, x=-4, y=-4, anchor="se")

root.mainloop()
