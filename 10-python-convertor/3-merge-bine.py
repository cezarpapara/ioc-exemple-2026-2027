# Convertor de unitati - varianta 3
# Rulare: python 3-merge-bine.py  (pe Windows: py 3-merge-bine.py)
import tkinter as tk
from tkinter import ttk, messagebox

NIVEL = ("Nivelul 3 din 4 – Merge bine (works well)",
         "Interfață clară și consecventă, cu feedback pentru fiecare acțiune, mesaje utile "
         "și aranjare responsivă.")
# unitate: (simbol, factor, decalaj); valoarea in unitatea de baza = valoare * factor + decalaj
UNITATI = {
    "Lungime": {"milimetru": ("mm", 0.001, 0), "centimetru": ("cm", 0.01, 0), "metru": ("m", 1, 0),
                "kilometru": ("km", 1000, 0), "inch": ("in", 0.0254, 0),
                "picior": ("ft", 0.3048, 0), "milă": ("mi", 1609.344, 0)},
    "Masă": {"gram": ("g", 0.001, 0), "kilogram": ("kg", 1, 0), "tonă": ("t", 1000, 0),
             "uncie": ("oz", 0.028349523125, 0), "livră": ("lb", 0.45359237, 0)},
    "Temperatură": {"grad Celsius": ("°C", 1, 0), "grad Fahrenheit": ("°F", 5 / 9, -160 / 9),
                    "kelvin": ("K", 1, -273.15)},
}
IMPLICIT = {"Lungime": (3, 6), "Masă": (1, 4), "Temperatură": (0, 1)}  # perechi uzuale
ARTICULAT = {"Lungime": "Lungimea", "Masă": "Masa"}
ROSU, VERDE, GRI = "#b00020", "#1e7b34", "#444444"


class ToolTip:
    """Bula de ajutor afisata cand mouse-ul sta deasupra unui widget."""
    def __init__(self, w, text):
        self.w, self.text, self.tip = w, text, None
        w.bind("<Enter>", self.arata)
        w.bind("<Leave>", self.ascunde)

    def arata(self, _e=None):
        self.tip = tk.Toplevel(self.w)
        self.tip.wm_overrideredirect(True)
        y = self.w.winfo_rooty() + self.w.winfo_height() + 4
        self.tip.wm_geometry(f"+{self.w.winfo_rootx() + 12}+{y}")
        tk.Label(self.tip, text=self.text, bg="#fffbe6", relief="solid", bd=1,
                 padx=6, pady=3).pack()

    def ascunde(self, _e=None):
        if self.tip:
            self.tip.destroy()
            self.tip = None


def numar(x):
    """Formateaza un numar romaneste: virgula zecimala, cel mult 4 zecimale."""
    text = f"{x:,.4f}".rstrip("0").rstrip(".") if abs(x) >= 0.001 or x == 0 else f"{x:.3g}"
    return text.replace(",", " ").replace(".", ",")


class Convertor:
    def __init__(self, root):
        root.title("Convertor de unități")
        root.minsize(440, 300)
        ttk.Style().theme_use("clam")
        f = ttk.Frame(root, padding=16)
        f.pack(fill="both", expand=True)
        f.columnconfigure(1, weight=1)
        # categoria: optiuni vizibile, nu de memorat
        self.v_cat = tk.StringVar(value="Lungime")
        cat = ttk.Frame(f)
        cat.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 12))
        ttk.Label(cat, text="Mărimea:").pack(side="left", padx=(0, 8))
        for nume in UNITATI:
            ttk.Radiobutton(cat, text=nume, value=nume, variable=self.v_cat,
                            command=self.schimba_categoria).pack(side="left", padx=4)
        # valoarea si unitatile
        ttk.Label(f, text="Valoarea:").grid(row=1, column=0, sticky="w")
        self.v_val = tk.StringVar(value="1")
        self.e_val = ttk.Entry(f, textvariable=self.v_val, width=14)
        self.e_val.grid(row=1, column=1, sticky="w", padx=(8, 0), pady=4)
        ToolTip(self.e_val, "Puteți folosi virgulă sau punct, de exemplu 12,5.")
        ttk.Label(f, text="Din:").grid(row=2, column=0, sticky="w")
        self.c_din = ttk.Combobox(f, state="readonly")
        self.c_din.grid(row=2, column=1, sticky="ew", padx=(8, 0), pady=4)
        ttk.Label(f, text="În:").grid(row=3, column=0, sticky="w")
        self.c_spre = ttk.Combobox(f, state="readonly")
        self.c_spre.grid(row=3, column=1, sticky="ew", padx=(8, 0), pady=4)
        b_inv = ttk.Button(f, text="⇅", width=3, command=self.inverseaza)
        b_inv.grid(row=2, column=2, rowspan=2, padx=(8, 0))
        ToolTip(b_inv, "Inversează unitățile")
        ttk.Button(f, text="Convertește", command=self.converteste).grid(
            row=4, column=0, columnspan=3, pady=10)
        # rezultatul si mesajele
        self.l_rez = ttk.Label(f, text="", font=("Segoe UI", 18, "bold"))
        self.l_rez.grid(row=5, column=0, columnspan=3, pady=6)
        self.l_stare = ttk.Label(f, text="Introduceți valoarea, alegeți unitățile și apăsați "
                                 "„Convertește” sau Enter.", foreground=GRI)
        self.l_stare.grid(row=6, column=0, columnspan=3, sticky="w")
        ttk.Button(f, text="Ce nivel are interfața?", command=self.arata_nivel).grid(
            row=7, column=1, columnspan=2, sticky="e", pady=(12, 0))
        root.bind("<Return>", lambda e: self.converteste())
        self.schimba_categoria()

    def mesaj(self, text, culoare=GRI):
        self.l_stare.config(text=text, foreground=culoare)

    def schimba_categoria(self):
        # unitatile se actualizeaza dupa marime: nu se pot alege unitati incompatibile
        nume = [f"{n} ({u[0]})" for n, u in UNITATI[self.v_cat.get()].items()]
        self.c_din.config(values=nume)
        self.c_spre.config(values=nume)
        self.c_din.current(IMPLICIT[self.v_cat.get()][0])
        self.c_spre.current(IMPLICIT[self.v_cat.get()][1])
        self.l_rez.config(text="")
        self.mesaj(f"Mărimea aleasă: {self.v_cat.get().lower()}. Alegeți unitățile.")

    def unitate(self, combo):
        return UNITATI[self.v_cat.get()][combo.get().rsplit(" (", 1)[0]]

    def inverseaza(self):
        din, spre = self.c_din.get(), self.c_spre.get()
        self.c_din.set(spre)
        self.c_spre.set(din)
        self.converteste()

    def converteste(self):
        try:
            x = float(self.v_val.get().strip().replace(",", "."))
        except ValueError:
            self.e_val.focus_set()
            return self.mesaj("Valoarea trebuie să fie un număr, de exemplu 12,5.", ROSU)
        (s1, f1, d1), (s2, f2, d2) = self.unitate(self.c_din), self.unitate(self.c_spre)
        baza = x * f1 + d1
        if self.v_cat.get() == "Temperatură" and baza < -273.15:
            return self.mesaj("Temperatura nu poate fi sub zero absolut (−273,15 °C).", ROSU)
        if self.v_cat.get() != "Temperatură" and x < 0:
            return self.mesaj(f"{ARTICULAT[self.v_cat.get()]} nu poate fi negativă.", ROSU)
        self.l_rez.config(text=f"{numar(x)} {s1} = {numar((baza - d2) / f2)} {s2}")
        self.mesaj("Conversie realizată.", VERDE)

    def arata_nivel(self):
        messagebox.showinfo("Ce nivel are interfața?", NIVEL[0] + "\n\n" + NIVEL[1] +
                            "\n\nComparați cu celelalte variante și cu fișa de lucru (FISA.md).")


if __name__ == "__main__":
    root = tk.Tk()
    Convertor(root)
    root.mainloop()
