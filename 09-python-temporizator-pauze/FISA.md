# Aplicația-exemplu 09 – Temporizator de pauze (Python, Tkinter)

**Ce face aplicația.** Un temporizator care îi amintește utilizatorului să ia pauze în timpul lucrului la calculator (de exemplu, 50 de minute de lucru urmate de 5 minute de pauză).
**Sarcina utilizatorului.** Setați 50 de minute de lucru și 5 minute de pauză, porniți temporizatorul, puneți-l pe pauză, reluați numărătoarea, apoi resetați. Observați ce se întâmplă la finalul etapei de lucru.
**Lecția din curs.** 02 – Factorul uman (atenția, oboseala, încărcarea cognitivă, modelul mental al utilizatorului).

## Cum se rulează

1. Aveți nevoie de Python 3 de pe [python.org](https://www.python.org/downloads/). Tkinter vine odată cu Python, nu se instalează nimic cu `pip`. (Pe Linux, dacă primiți eroarea `No module named 'tkinter'`, instalați pachetul `python3-tk`.)
2. Deschideți folderul `09-python-temporizator-pauze` în VS Code, apoi un terminal (**Terminal → New Terminal**).
3. Rulați câte o variantă:
   ```
   python 3-merge-bine.py
   ```
   Pe Windows: `py 3-merge-bine.py`. Puteți folosi și butonul **Run** din VS Code (cu extensia Python instalată).

**Constanta `VITEZA`.** Ca să nu așteptați 50 de minute, fiecare fișier are la început linia `VITEZA = 1` (timp real). Pentru test, schimbați-o în `VITEZA = 60`: un minut trece într-o secundă, deci etapa de lucru de 50 de minute durează 50 de secunde, iar pauza de 5 minute durează 5 secunde. Reveniți la `VITEZA = 1` când terminați.

## Ce aveți de făcut

1. Rulați cele patru variante **în ordine aleatorie** (nu în ordinea numerelor din nume).
2. Pentru fiecare variantă, încercați sarcina de mai sus și notați în tabel ce vă ajută și ce vă încurcă.
3. Pentru fiecare problemă, numiți euristica sau principiul încălcat (Nielsen, feedback, prevenirea erorilor, vizibilitatea stării, modelul mental, contrast, ținte mici etc.).
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
   - etichete în română, consecvente și cu unitate de măsură („Durata lucrului (minute)”, „Durata pauzei (minute)”), cu valorile implicite 50 și 5;
   - mesaje de eroare care spun ce este greșit și cum se corectează, în locul „Invalid input” și „Error 42”, afișate într-o etichetă de stare;
   - butoane activate doar când au sens (Start dezactivat cât timp temporizatorul rulează), iar butonul de pauză își schimbă textul în „Continuă”;
   - mesaje diferite la finalul lucrului și la finalul pauzei, care spun ce urmează („Faceți o pauză de 5 minute…”);
   - butonul de resetare mutat departe de Start și fără roșu strident; tooltips pentru butoane;
   - `grid()` cu `columnconfigure(..., weight=1)` în locul coordonatelor fixe din `place()`, ca fereastra să se poată redimensiona.
2. ★ Refaceți varianta 1 de la zero, păstrând aceeași funcționalitate.
3. ★ Adăugați o funcționalitate la varianta 4: programe predefinite (de exemplu 25 / 5, metoda Pomodoro), o temă întunecată sau salvarea setărilor într-un fișier JSON.

> Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

---

## Ghid pentru cadrul didactic (citiți după ce ați completat tabelul)

**Nivelul 1 – Nu merge.** Câmpul „Timp” nu are unitate (cere secunde, deși utilizatorul se gândește la minute); butoane-simbol ▶ și ■, mici și fără tooltips; ■ închide aplicația fără confirmare; ▶ apăsat de două ori pornește două numărători, iar timpul curge de două ori mai repede; nu există pauză; timpul apare în secunde brute, gri pe gri (contrast slab); etapa este „mod 1” / „mod 2” (cod intern expus utilizatorului); la finalul lucrului nu apare niciun anunț; pauza este fixă (300 s) și nu apare nicăieri; o valoare greșită este ignorată în tăcere; fereastră fixă, text de 7 pt.

**Nivelul 2 – Merge.** Funcționează (mm:ss, Start, Pauza, Reset), dar: etichete amestecate în engleză și română, fără unitate la pauză și fără valori implicite; mesaje tehnice („Invalid input”, „Error 42”); Start apăsat în timpul numărătorii reîncepe de la zero fără avertisment, deci după Pauza utilizatorul pierde progresul dacă apasă Start; butonul Pauza nu își schimbă textul (starea nu se vede); Reset roșu, lângă Start, fără confirmare; „Time is up!” apare identic la ambele etape, într-o fereastră modală care oprește numărătoarea până la OK; poziții fixe cu `place()`.

**Nivelul 3 – Merge bine.** `ttk`, etichete clare cu unități, valori implicite 50 / 5 și limite în Spinbox; etapa colorată (Lucru albastru, Pauză verde), timp mare, bară de progres, numărul ciclului; butoanele sunt active doar când au sens, „Pune pe pauză” devine „Continuă”; mesaje de stare (succes verde, eroare roșie, informare gri) și tooltips; la final, o alertă clară, cu indicații de ergonomie; `grid()`, fereastră redimensionabilă.

**Nivelul 4 – Merge foarte bine.** În plus: câmpurile acceptă doar cifre (eroarea este prevenită, nu doar semnalată); resetarea cere confirmare, cu „Nu” ca opțiune implicită; schimbarea etapei este anunțată nemodal (banner colorat, sunet, fereastra adusă în față), fără să blocheze numărătoarea; timpul rămas apare și în titlul ferestrei, deci în bara de activități; focusul este gestionat (după Pornește, focusul trece pe butonul de pauză; Spațiu sau Enter acționează butonul), scurtături Ctrl+R și Esc, anunțate pe ecran; culori cu contrast verificat (WCAG AA), font mai mare, inel de focus colorat; ora la care a început etapa apare în mesajul de stare.

*Observație pentru discuție:* pe Linux, Tkinter afișează butoanele dialogurilor în engleză („Yes” / „No”), iar pe Windows în limba sistemului. Este un exemplu de inconsecvență care nu ține de programator, ci de platformă.
