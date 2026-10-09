# Temporizator de pauze - varianta 4
# Rulare: python 4-merge-foarte-bine.py  (pe Windows: py 4-merge-foarte-bine.py)
import time
import tkinter as tk
from tkinter import ttk, messagebox

VITEZA = 1  # 1 = timp real; 60 = un minut trece intr-o secunda (doar pentru test)

NIVEL = ("Nivelul 4 din 4 – Merge foarte bine (works very well)",
         "În plus: accesibilitate, prevenirea erorilor, navigare cu tastatura și detalii de finețe.")
# culori verificate pentru contrast de minimum 4,5:1 fata de fundal (WCAG AA)
C = dict(bg="#f5f6f8", fg="#1b1d21", lucru="#1f5fa8", pauza="#1e7b34", eroare="#b00020",
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


class Temporizator:
    def __init__(self, root):
        self.root, self.job, self.ruleaza = root, None, False
        self.lucru, self.pauza_min, self.cicluri = 50, 5, 1
        root.title("Temporizator de pauze")
        root.minsize(430, 360)
        root.configure(bg=C["bg"])
        self.stil = ttk.Style()
        self.stil.theme_use("clam")
        self.stil.configure(".", font=("Segoe UI", 11), background=C["bg"], foreground=C["fg"],
                            focuscolor=C["lucru"])  # focus vizibil, in culoarea aplicatiei
        self.stil.configure("TButton", padding=(12, 4))
        f = ttk.Frame(root, padding=18)
        f.pack(fill="both", expand=True)
        f.columnconfigure(1, weight=1)
        # anunt nemodal la schimbarea etapei (nu blocheaza fereastra ca un messagebox)
        self.banner = tk.Label(f, font=("Segoe UI", 11, "bold"), fg="#ffffff", padx=10, pady=8)
        # campurile accepta doar cifre (cel mult 3): literele nici nu pot fi tastate
        cifre = (root.register(lambda t: t == "" or (t.isdigit() and len(t) <= 3)), "%P")
        self.v_lucru, self.v_pauza = tk.StringVar(value="50"), tk.StringVar(value="5")
        self.spin = []
        for r, (text, var, maxim, ajutor) in enumerate((
                ("Lucru (minute, 1–120):", self.v_lucru, 120, "Recomandat: 50 de minute"),
                ("Pauză (minute, 1–30):", self.v_pauza, 30, "Recomandat: 5–10 minute")), 1):
            ttk.Label(f, text=text).grid(row=r, column=0, sticky="w", pady=3)
            self.spin.append(ttk.Spinbox(f, from_=1, to=maxim, width=6, textvariable=var,
                                         validate="key", validatecommand=cifre))
            self.spin[-1].grid(row=r, column=1, sticky="w", padx=(8, 0))
            ToolTip(self.spin[-1], ajutor)
        self.l_etapa = ttk.Label(f, font=("Segoe UI", 14, "bold"))
        self.l_etapa.grid(row=3, column=0, columnspan=2, pady=(14, 0))
        self.l_timp = ttk.Label(f, font=("Segoe UI", 44, "bold"))
        self.l_timp.grid(row=4, column=0, columnspan=2)
        self.bara = ttk.Progressbar(f, maximum=1000, style="Etapa.Horizontal.TProgressbar")
        self.bara.grid(row=5, column=0, columnspan=2, sticky="ew", pady=6)
        b = ttk.Frame(f)
        b.grid(row=6, column=0, columnspan=2, pady=10)
        self.b_start = ttk.Button(b, text="Pornește", command=self.porneste)
        self.b_pauza = ttk.Button(b, text="Pune pe pauză", command=self.pauza)
        self.b_reset = ttk.Button(b, text="Resetează…", command=self.reseteaza)
        for i, (btn, ajutor) in enumerate(((self.b_start, "Pornește lucrul (Enter sau Spațiu)"),
                                           (self.b_pauza, "Oprește temporar sau reia (Spațiu)"),
                                           (self.b_reset, "Oprește și revine la setări (Ctrl+R)"))):
            btn.grid(row=0, column=i, padx=4, ipady=3)
            ToolTip(btn, ajutor)
        self.l_stare = ttk.Label(f, wraplength=390)
        self.l_stare.grid(row=7, column=0, columnspan=2, sticky="w")
        ttk.Button(f, text="Ce nivel are interfața?", command=self.arata_nivel).grid(
            row=8, column=1, sticky="e", pady=(12, 0))
        # scurtaturi: Enter apasa butonul cu focus, Ctrl+R reseteaza, Esc inchide anuntul
        root.bind("<Return>", lambda e: isinstance(e.widget, ttk.Button) and e.widget.invoke())
        root.bind("<Control-r>", lambda e: self.reseteaza())
        root.bind("<Escape>", lambda e: self.banner.grid_remove())
        self.seteaza_etapa("lucru")
        self.afiseaza()
        self.activ(False)
        self.mesaj("Apăsați „Pornește” (sau Enter). Ctrl+R resetează, Esc închide anunțurile.")

    def mesaj(self, text, culoare="slab"):
        self.l_stare.config(text=text, foreground=C[culoare])

    def activ(self, da):
        # activeaza doar comenzile care au sens; focusul trece pe urmatoarea comanda (Spatiu/Enter)
        for w in (*self.spin, self.b_start):
            w.state(["disabled" if da else "!disabled"])
        for w in (self.b_pauza, self.b_reset):
            w.state(["!disabled" if da else "disabled"])
        self.b_pauza.config(text="Pune pe pauză")
        (self.b_pauza if da else self.b_start).focus_set()

    def porneste(self):
        self.lucru, self.pauza_min = int(self.v_lucru.get() or 0), int(self.v_pauza.get() or 0)
        if not (1 <= self.lucru <= 120 and 1 <= self.pauza_min <= 30):
            return self.mesaj("Lucrul poate dura 1–120 de minute, iar pauza 1–30. "
                              "Corectați valorile din câmpuri.", "eroare")
        self.ruleaza, self.cicluri = True, 1
        self.seteaza_etapa("lucru")
        self.activ(True)
        self.mesaj(f"A pornit: {self.lucru} min de lucru, apoi {self.pauza_min} min de pauză.", "pauza")
        self.tic()

    def seteaza_etapa(self, etapa, anunt=None):
        self.etapa = etapa
        self.ramas = self.total = (self.lucru if etapa == "lucru" else self.pauza_min) * 60
        nume = "Lucru" if etapa == "lucru" else "Pauză"
        self.l_etapa.config(text=f"{nume} · ciclul {self.cicluri}", foreground=C[etapa])
        self.stil.configure("Etapa.Horizontal.TProgressbar", background=C[etapa])
        if anunt:  # semnal discret: sunet, fereastra in fata, anunt inchis cu Esc
            self.root.bell()
            self.root.lift()
            ora = time.strftime("%H:%M")
            self.mesaj(f"{'Lucrul' if etapa == 'lucru' else 'Pauza'} a început la {ora}.", etapa)
            self.banner.config(text=anunt + "  (Esc închide anunțul)", bg=C[etapa])
            self.banner.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

    def tic(self):
        if self.ramas <= 0 and self.etapa == "lucru":
            self.seteaza_etapa("pauza", f"Pauză de {self.pauza_min} min: ridicați-vă și "
                                        "priviți în depărtare.")
        elif self.ramas <= 0:
            self.cicluri += 1
            self.seteaza_etapa("lucru", "Pauza s-a încheiat. Începe o nouă etapă de lucru.")
        # timpul ramas apare si in titlu, deci si in bara de activitati
        self.root.title(f"{self.afiseaza()} · {self.l_etapa['text']}")
        self.ramas -= 1
        self.job = self.root.after(max(1, 1000 // VITEZA), self.tic)

    def afiseaza(self):
        text = f"{self.ramas // 60:02d}:{self.ramas % 60:02d}"
        self.l_timp.config(text=text)
        self.bara["value"] = 1000 * (self.total - self.ramas) / self.total
        return text

    def pauza(self):
        if self.ruleaza:
            self.root.after_cancel(self.job)
            self.mesaj("Temporizatorul este oprit temporar. Apăsați „Continuă” sau Spațiu.")
        else:
            self.mesaj("Numărătoarea a fost reluată.", "pauza")
            self.tic()
        self.ruleaza = not self.ruleaza
        self.b_pauza.config(text="Pune pe pauză" if self.ruleaza else "Continuă")

    def reseteaza(self):
        if self.job is None or not messagebox.askyesno(
                "Resetați temporizatorul?", "Progresul etapei curente se va pierde. Continuați?",
                icon="warning", default="no"):
            return  # nimic de resetat sau utilizatorul a renuntat
        self.root.after_cancel(self.job)
        self.ruleaza, self.job, self.cicluri = False, None, 1
        self.banner.grid_remove()
        self.seteaza_etapa("lucru")
        self.afiseaza()
        self.root.title("Temporizator de pauze")
        self.activ(False)
        self.mesaj("Temporizatorul a fost resetat. Setările au rămas aceleași.")

    def arata_nivel(self):
        messagebox.showinfo("Ce nivel are interfața?", NIVEL[0] + "\n\n" + NIVEL[1] +
                            "\n\nComparați cu celelalte variante și cu fișa de lucru (FISA.md).")


if __name__ == "__main__":
    root = tk.Tk()
    Temporizator(root)
    root.mainloop()
