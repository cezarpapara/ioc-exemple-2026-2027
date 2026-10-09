# Aplicația-exemplu 10 – Convertor de unități (Python, Tkinter)

**Ce face aplicația.** Transformă o valoare dintr-o unitate de măsură în alta, pentru trei mărimi: lungime, masă și temperatură.
**Sarcina utilizatorului.** Aflați (1) câte mile înseamnă 5 km, (2) cât înseamnă 37 °C în grade Fahrenheit și (3) ce se întâmplă dacă scrieți 1,5 (cu virgulă) sau o temperatură sub zero absolut, de exemplu −300 °C.
**Lecția din curs.** 06 – Principii și ghiduri de proiectare (euristicile lui Nielsen, prevenirea erorilor, consecvența, recunoaștere în loc de reamintire).

## Cum se rulează

1. Aveți nevoie de Python 3 de pe [python.org](https://www.python.org/downloads/). Tkinter vine odată cu Python, nu se instalează nimic cu `pip`. (Pe Linux, dacă primiți eroarea `No module named 'tkinter'`, instalați pachetul `python3-tk`.)
2. Deschideți folderul `10-python-convertor` în VS Code, apoi un terminal (**Terminal → New Terminal**).
3. Rulați câte o variantă:
   ```
   python 3-merge-bine.py
   ```
   Pe Windows: `py 3-merge-bine.py`. Puteți folosi și butonul **Run** din VS Code (cu extensia Python instalată).

## Ce aveți de făcut

1. Rulați cele patru variante **în ordine aleatorie** (nu în ordinea numerelor din nume).
2. Pentru fiecare variantă, încercați cele trei sarcini de mai sus și notați în tabel ce vă ajută și ce vă încurcă.
3. Pentru fiecare problemă, numiți euristica sau principiul încălcat (de exemplu: prevenirea erorilor, mesaje de eroare clare, consecvență și standarde, potrivirea cu lumea reală, recunoaștere în loc de reamintire, vizibilitatea stării, contrast).
4. Ghiciți nivelul (1–4) și abia apoi apăsați butonul **„Ce nivel are interfața?”** din colțul ferestrei.

## Tabel de observație (de completat)

| Varianta | Ce funcționează | Ce încurcă | Euristica sau principiul încălcat | Nivelul ghicit |
|---|---|---|---|---|
| 1-nu-merge.py | | | | |
| 2-merge.py | | | | |
| 3-merge-bine.py | | | | |
| 4-merge-foarte-bine.py | | | | |

## Exerciții

1. **Îmbunătățiți varianta 2 până la nivelul 3:**
   - alegerea mărimii (lungime, masă, temperatură) cu butoane radio, iar listele de unități filtrate după mărime, ca să nu mai poată fi alese unități incompatibile;
   - acceptarea virgulei zecimale (`text.replace(",", ".")`) și afișarea rezultatului cu unități, de exemplu „5 km = 3,1069 mi”;
   - mesaje care spun ce este greșit și cum se corectează, în locul „Invalid input” și „Error 42”, afișate într-o etichetă de stare, nu în ferestre modale;
   - etichete în română, consecvente („Valoarea”, „Din”, „În”, „Convertește”) și simboluri corecte (°C, °F, K);
   - verificarea limitelor fizice: temperatura nu poate coborî sub zero absolut, lungimea și masa nu pot fi negative;
   - conversie și la apăsarea tastei Enter; `grid()` în locul coordonatelor fixe din `place()`.
2. ★ Refaceți varianta 1 de la zero, păstrând aceeași funcționalitate.
3. ★ Adăugați o funcționalitate la varianta 4: o mărime nouă (volum: litru, mililitru, galon; sau viteză: km/h, m/s, mph), salvarea istoricului într-un fișier sau o temă întunecată.

> Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

---

## Ghid pentru cadrul didactic (citiți după ce ați completat tabelul)

**Nivelul 1 – Nu merge.** Un câmp fără etichetă; conversiile sunt coduri criptice („C-F”, „km-mi”, „lb-kg”) într-o listă neordonată, iar unele lipsesc (există „C-K”, dar nu și „K-C”); butoanele „=” și „C” sunt minuscule și lipite, iar „C” șterge tot (alunecare ușoară, fără confirmare); rezultatul apare cu 16 zecimale, fără unitate, gri deschis pe fundal deschis; o valoare cu virgulă („1,5”) sau un text sunt ignorate fără niciun mesaj; titlul ferestrei este „Conv”.

**Nivelul 2 – Merge.** Pentru valori corecte, conversia funcționează, dar: etichete amestecate („From”, „in”, „Convert”, „Result”, „Valoare”); simboluri ambigue („C”, „F”); listele conțin toate unitățile, deci se poate alege m → kg, iar eroarea apare abia după aceea („Error 42: incompatible units”), în loc să fie prevenită; virgula zecimală produce „Invalid input”; rezultatul are 2 zecimale și nu are unitate; o temperatură imposibilă este acceptată (−500 K devine −773,15); Enter nu face nimic; poziții fixe cu `place()`.

**Nivelul 3 – Merge bine.** Mărimea se alege cu butoane radio (opțiunile se văd, nu trebuie reamintite); listele de unități se actualizează după mărime, cu denumiri complete și simboluri; perechi implicite uzuale (km → mi, kg → lb, °C → °F); virgula este acceptată; rezultatul este formatat românește și cu unități („37 °C = 98,6 °F”); mesaje de stare pentru eroare (număr greșit, valori negative, zero absolut), succes și informare; buton ⇅ pentru inversarea unităților, cu tooltip; Enter pornește conversia; `grid()`, fereastră redimensionabilă.

**Nivelul 4 – Merge foarte bine.** În plus: rezultatul se actualizează pe măsură ce utilizatorul scrie; câmpul acceptă doar caractere care pot forma un număr (eroarea este prevenită); o linie de referință („1 km = 0,6214 mi”, respectiv „0 °C = 32 °F” la temperatură) ajută utilizatorul să verifice rezultatul; istoricul ultimelor 5 conversii (Enter), cu „Golește istoricul…” care cere confirmare, cu „Nu” ca opțiune implicită; copierea rezultatului, cu mesaj de confirmare; scurtături Alt+L/M/T (literele subliniate), Ctrl+I și Esc, anunțate pe ecran; focusul pornește din câmpul de valoare; culori cu contrast verificat (WCAG AA), font mai mare, inel de focus colorat.

*Observație pentru discuție:* pe Linux, Tkinter afișează butoanele dialogurilor în engleză („Yes” / „No”), iar pe Windows în limba sistemului. Este un exemplu de inconsecvență care nu ține de programator, ci de platformă.
