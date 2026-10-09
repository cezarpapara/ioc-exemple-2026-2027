# Convertor de unitati - varianta 4
# Rulare: python 4-merge-foarte-bine.py  (pe Windows: py 4-merge-foarte-bine.py)
import re
import tkinter as tk
from tkinter import ttk, messagebox

NIVEL = ("Nivelul 4 din 4 – Merge foarte bine (works very well)",
         "În plus: accesibilitate, prevenirea erorilor, navigare cu tastatura și detalii de finețe.")
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
# culori verificate pentru contrast de minimum 4,5:1 fata de fundal (WCAG AA)
C = dict(bg="#f5f6f8", fg="#1b1d21", accent="#1f5fa8", ok="#1e7b34", eroare="#b00020",
         slab="#4a4f57")


class ToolTip:
    """Bula de ajutor afisata cand mouse-ul sta deasupra unui widget."""
    def __init__(self, w, text):
        self.w, self.text, self.tip = w, text, None
        w.bind("<Enter>", self.arata, add="+")
        w.bind("<Leave>", self.ascunde, add="+")

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
        self.root = root
        root.title("Convertor de unități")
        root.minsize(470, 420)
        root.configure(bg=C["bg"])
        st = ttk.Style()
        st.theme_use("clam")
        st.configure(".", font=("Segoe UI", 11), background=C["bg"], foreground=C["fg"],
                     focuscolor=C["accent"])  # focus vizibil
        st.map("TCombobox", fieldbackground=[("readonly", "#ffffff")])
        f = ttk.Frame(root, padding=18)
        f.pack(fill="both", expand=True)
        f.columnconfigure(1, weight=1)
        # categoria: Alt + litera subliniata
        self.v_cat = tk.StringVar(value="Lungime")
        cat = ttk.Frame(f)
        cat.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 12))
        ttk.Label(cat, text="Mărimea:").pack(side="left", padx=(0, 8))
        for nume in UNITATI:
            ttk.Radiobutton(cat, text=nume, value=nume, variable=self.v_cat, underline=0,
                            command=self.schimba_categoria).pack(side="left", padx=4)
            root.bind(f"<Alt-{nume[0].lower()}>", lambda e, n=nume: (self.v_cat.set(n),
                                                                     self.schimba_categoria()))
        # campul accepta doar caractere care pot forma un numar (prevenirea erorilor)
        valid = (root.register(lambda t: re.fullmatch(r"-?\d*[.,]?\d*", t) is not None), "%P")
        ttk.Label(f, text="Valoarea:").grid(row=1, column=0, sticky="w")
        self.v_val = tk.StringVar(value="1")
        self.e_val = ttk.Entry(f, textvariable=self.v_val, width=14, validate="key",
                               validatecommand=valid)
        self.e_val.grid(row=1, column=1, sticky="w", padx=(8, 0), pady=4)
        ToolTip(self.e_val, "Rezultatul se actualizează pe măsură ce scrieți (virgulă sau punct).")
        self.combo = []
        for r, text in ((2, "Din:"), (3, "În:")):
            ttk.Label(f, text=text).grid(row=r, column=0, sticky="w")
            self.combo.append(ttk.Combobox(f, state="readonly"))
            self.combo[-1].grid(row=r, column=1, sticky="ew", padx=(8, 0), pady=4)
            self.combo[-1].bind("<<ComboboxSelected>>", lambda e: self.converteste())
        b_inv = ttk.Button(f, text="⇅", width=3, command=self.inverseaza)
        b_inv.grid(row=2, column=2, rowspan=2, padx=(8, 0))
        ToolTip(b_inv, "Inversează unitățile (Ctrl+I)")
        # rezultatul, echivalenta de referinta si mesajele
        self.l_rez = ttk.Label(f, font=("Segoe UI", 20, "bold"), foreground=C["accent"])
        self.l_rez.grid(row=4, column=0, columnspan=3, pady=(12, 0))
        self.l_ref = ttk.Label(f, foreground=C["slab"])
        self.l_ref.grid(row=5, column=0, columnspan=3)
        self.l_stare = ttk.Label(f, wraplength=420)
        self.l_stare.grid(row=6, column=0, columnspan=3, sticky="w", pady=(8, 0))
        b = ttk.Frame(f)
        b.grid(row=7, column=0, columnspan=3, sticky="ew", pady=8)
        ttk.Button(b, text="Copiază rezultatul", command=self.copiaza).pack(side="left")
        ttk.Button(b, text="Golește istoricul…", command=self.goleste).pack(side="right")
        self.istoric = tk.Listbox(f, height=4, font=("Segoe UI", 10), activestyle="none",
                                  highlightcolor=C["accent"])
        self.istoric.grid(row=8, column=0, columnspan=3, sticky="nsew")
        f.rowconfigure(8, weight=1)
        ttk.Label(f, text="Enter – salvează în istoric · Ctrl+I – inversează · Esc – golește "
                  "câmpul · Alt+L/M/T – mărimea", foreground=C["slab"], font=("Segoe UI", 9)).grid(
            row=9, column=0, columnspan=3, sticky="w", pady=(6, 0))
        ttk.Button(f, text="Ce nivel are interfața?", command=self.arata_nivel).grid(
            row=10, column=1, columnspan=2, sticky="e", pady=(8, 0))
        root.bind("<Return>", lambda e: self.salveaza())
        root.bind("<Control-i>", lambda e: self.inverseaza())
        root.bind("<Escape>", lambda e: (self.v_val.set(""), self.e_val.focus_set()))
        self.v_val.trace_add("write", lambda *a: self.converteste())
        self.schimba_categoria()
        self.e_val.focus_set()

    def mesaj(self, text, culoare="slab"):
        self.l_stare.config(text=text, foreground=C[culoare])

    def schimba_categoria(self):
        # unitatile se actualizeaza dupa marime: nu se pot alege unitati incompatibile
        nume = [f"{n} ({u[0]})" for n, u in UNITATI[self.v_cat.get()].items()]
        for combo, implicit in zip(self.combo, IMPLICIT[self.v_cat.get()]):
            combo.config(values=nume)
            combo.current(implicit)
        self.converteste()

    def inverseaza(self):
        din, spre = self.combo[0].get(), self.combo[1].get()
        self.combo[0].set(spre)
        self.combo[1].set(din)
        self.converteste()

    def converteste(self):
        self.rezultat = None
        text = self.v_val.get().replace(",", ".")
        cat = self.v_cat.get()
        (s1, f1, d1), (s2, f2, d2) = [UNITATI[cat][c.get().rsplit(" (", 1)[0]] for c in self.combo]
        conv = lambda v: ((v * f1 + d1) - d2) / f2
        self.l_ref.config(text=f"Referință: 1 {s1} = {numar(conv(1))} {s2}" if d1 == d2 == 0
                          else f"Referință: 0 {s1} = {numar(conv(0))} {s2}")
        if text in ("", "-", "."):
            self.l_rez.config(text="–")
            return self.mesaj("Scrieți o valoare; rezultatul apare imediat.")
        x = float(text)
        if cat == "Temperatură" and x * f1 + d1 < -273.15:
            self.l_rez.config(text="–")
            return self.mesaj("Temperatura nu poate fi sub zero absolut (−273,15 °C).", "eroare")
        if cat != "Temperatură" and x < 0:
            self.l_rez.config(text="–")
            return self.mesaj(f"{ARTICULAT[cat]} nu poate fi negativă.", "eroare")
        self.rezultat = f"{numar(x)} {s1} = {numar(conv(x))} {s2}"
        self.l_rez.config(text=self.rezultat)
        self.mesaj("Apăsați Enter pentru a păstra conversia în istoric.")

    def salveaza(self):
        if self.rezultat:
            self.istoric.insert(0, self.rezultat)
            self.istoric.delete(5, "end")  # pastram ultimele 5 conversii
            self.mesaj("Conversia a fost salvată în istoric.", "ok")

    def copiaza(self):
        if self.rezultat:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.rezultat)
            self.mesaj(f"Am copiat: {self.rezultat}", "ok")
        else:
            self.mesaj("Nu există încă un rezultat de copiat.", "eroare")

    def goleste(self):
        if self.istoric.size() and messagebox.askyesno(
                "Goliți istoricul?", "Se vor șterge toate conversiile salvate.", icon="warning",
                default="no"):
            self.istoric.delete(0, "end")
            self.mesaj("Istoricul a fost golit.", "ok")

    def arata_nivel(self):
        messagebox.showinfo("Ce nivel are interfața?", NIVEL[0] + "\n\n" + NIVEL[1] +
                            "\n\nComparați cu celelalte variante și cu fișa de lucru (FISA.md).")


if __name__ == "__main__":
    root = tk.Tk()
    Convertor(root)
    root.mainloop()
