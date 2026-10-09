# Temporizator de pauze - varianta 3
# Rulare: python 3-merge-bine.py  (pe Windows: py 3-merge-bine.py)
import tkinter as tk
from tkinter import ttk, messagebox

VITEZA = 1  # 1 = timp real; 60 = un minut trece intr-o secunda (doar pentru test)

NIVEL = ("Nivelul 3 din 4 – Merge bine (works well)",
         "Interfață clară și consecventă, cu feedback pentru fiecare acțiune, mesaje utile "
         "și aranjare responsivă.")
ALBASTRU, VERDE, ROSU, GRI = "#1f5fa8", "#1e7b34", "#b00020", "#444444"


class ToolTip:
    """Bula de ajutor afisata cand mouse-ul sta deasupra unui widget."""
    def __init__(self, widget, text):
        self.widget, self.text, self.tip = widget, text, None
        widget.bind("<Enter>", self.arata)
        widget.bind("<Leave>", self.ascunde)

    def arata(self, _e=None):
        x = self.widget.winfo_rootx() + 12
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 4
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        self.tip.wm_geometry(f"+{x}+{y}")
        tk.Label(self.tip, text=self.text, bg="#fffbe6", relief="solid", bd=1,
                 padx=6, pady=3, wraplength=260, justify="left").pack()

    def ascunde(self, _e=None):
        if self.tip:
            self.tip.destroy()
            self.tip = None


class Temporizator:
    def __init__(self, root):
        self.root, self.job, self.ruleaza, self.cicluri = root, None, False, 1
        self.lucru, self.pauza_min = 50, 5
        root.title("Temporizator de pauze")
        root.minsize(380, 330)
        stil = ttk.Style()
        stil.theme_use("clam")
        stil.configure("Horizontal.TProgressbar", background=ALBASTRU)
        f = ttk.Frame(root, padding=16)
        f.pack(fill="both", expand=True)
        f.columnconfigure(1, weight=1)
        # setarile: duratele in minute, cu limite si valori implicite
        self.v_lucru, self.v_pauza = tk.StringVar(value="50"), tk.StringVar(value="5")
        self.spin = []
        for r, (text, var, maxim, ajutor) in enumerate((
                ("Durata lucrului (minute):", self.v_lucru, 120, "Între 1 și 120. Recomandat: 50."),
                ("Durata pauzei (minute):", self.v_pauza, 30, "Între 1 și 30. Recomandat: 5–10."))):
            ttk.Label(f, text=text).grid(row=r, column=0, sticky="w", pady=3)
            s = ttk.Spinbox(f, from_=1, to=maxim, width=6, textvariable=var)
            s.grid(row=r, column=1, sticky="w", padx=(8, 0))
            ToolTip(s, ajutor)
            self.spin.append(s)
        # afisajul: etapa, timpul ramas, progresul
        self.l_etapa = ttk.Label(f, font=("Segoe UI", 13, "bold"))
        self.l_etapa.grid(row=2, column=0, columnspan=2, pady=(14, 0))
        self.l_timp = ttk.Label(f, text="50:00", font=("Segoe UI", 40, "bold"))
        self.l_timp.grid(row=3, column=0, columnspan=2)
        self.bara = ttk.Progressbar(f, maximum=1000)
        self.bara.grid(row=4, column=0, columnspan=2, sticky="ew", pady=6)
        # comenzi, activate doar cand au sens
        b = ttk.Frame(f)
        b.grid(row=5, column=0, columnspan=2, pady=10)
        self.b_start = ttk.Button(b, text="Pornește", command=self.porneste)
        self.b_pauza = ttk.Button(b, text="Pune pe pauză", command=self.pauza)
        self.b_reset = ttk.Button(b, text="Resetează", command=self.reseteaza)
        for i, (btn, ajutor) in enumerate((
                (self.b_start, "Pornește numărătoarea pentru etapa de lucru."),
                (self.b_pauza, "Oprește temporar numărătoarea; o puteți relua oricând."),
                (self.b_reset, "Oprește temporizatorul și revine la valorile setate."))):
            btn.grid(row=0, column=i, padx=4)
            ToolTip(btn, ajutor)
        self.l_stare = ttk.Label(f, text="Setați duratele și apăsați „Pornește”.", foreground=GRI)
        self.l_stare.grid(row=6, column=0, columnspan=2, sticky="w")
        ttk.Button(f, text="Ce nivel are interfața?", command=self.arata_nivel).grid(
            row=7, column=1, sticky="e", pady=(10, 0))
        self.activ(False)
        self.seteaza_etapa("lucru")

    def mesaj(self, text, culoare=GRI):
        self.l_stare.config(text=text, foreground=culoare)

    def activ(self, da):
        # setarile se blocheaza cat timp temporizatorul ruleaza
        for w in (*self.spin, self.b_start):
            w.config(state="disabled" if da else "normal")
        self.b_pauza.config(state="normal" if da else "disabled", text="Pune pe pauză")
        self.b_reset.config(state="normal" if da else "disabled")

    def porneste(self):
        try:
            self.lucru, self.pauza_min = int(self.v_lucru.get()), int(self.v_pauza.get())
        except ValueError:
            self.lucru = self.pauza_min = 0
        if not (1 <= self.lucru <= 120 and 1 <= self.pauza_min <= 30):
            self.mesaj("Lucrul poate dura între 1 și 120 de minute, iar pauza între 1 și 30.", ROSU)
            return
        self.ruleaza, self.cicluri = True, 1
        self.seteaza_etapa("lucru")
        self.activ(True)
        self.mesaj(f"A pornit: {self.lucru} min de lucru, apoi {self.pauza_min} min de pauză.", VERDE)
        self.tic()

    def seteaza_etapa(self, etapa):
        self.etapa = etapa
        self.ramas = self.total = (self.lucru if etapa == "lucru" else self.pauza_min) * 60
        if etapa == "lucru":
            self.l_etapa.config(text=f"Lucru · ciclul {self.cicluri}", foreground=ALBASTRU)
        else:
            self.l_etapa.config(text="Pauză – ridicați-vă și relaxați ochii", foreground=VERDE)

    def tic(self):
        if self.ramas <= 0:
            self.root.bell()
            if self.etapa == "lucru":
                messagebox.showinfo("E timpul pentru o pauză",
                                    f"Ați lucrat {self.lucru} minute. Faceți o pauză de "
                                    f"{self.pauza_min} minute: ridicați-vă, întindeți-vă "
                                    "și priviți în depărtare.")
                self.seteaza_etapa("pauza")
            else:
                self.cicluri += 1
                self.mesaj("Pauza s-a încheiat. A început o nouă etapă de lucru.", ALBASTRU)
                self.seteaza_etapa("lucru")
        self.l_timp.config(text=f"{self.ramas // 60:02d}:{self.ramas % 60:02d}")
        self.bara["value"] = 1000 * (self.total - self.ramas) / self.total
        self.ramas -= 1
        self.job = self.root.after(max(1, 1000 // VITEZA), self.tic)

    def pauza(self):
        if self.ruleaza:
            self.root.after_cancel(self.job)
            self.mesaj("Temporizatorul este oprit temporar. Apăsați „Continuă” pentru a relua.")
        else:
            self.mesaj("Numărătoarea a fost reluată.", VERDE)
            self.tic()
        self.ruleaza = not self.ruleaza
        self.b_pauza.config(text="Pune pe pauză" if self.ruleaza else "Continuă")

    def reseteaza(self):
        self.root.after_cancel(self.job)
        self.ruleaza, self.cicluri = False, 1
        self.activ(False)
        self.seteaza_etapa("lucru")
        self.l_timp.config(text=f"{self.lucru:02d}:00")
        self.bara["value"] = 0
        self.mesaj("Temporizatorul a fost resetat.")

    def arata_nivel(self):
        messagebox.showinfo("Ce nivel are interfața?", NIVEL[0] + "\n\n" + NIVEL[1] +
                            "\n\nComparați cu celelalte variante și cu fișa de lucru (FISA.md).")


if __name__ == "__main__":
    root = tk.Tk()
    Temporizator(root)
    root.mainloop()
