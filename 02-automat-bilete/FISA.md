# Aplicația-exemplu 02 – Automat de bilete de autobuz

**Ce face aplicația.** Simulează un automat de bilete: alegeți tipul biletului, categoria de călător și numărul de bilete, vedeți prețul și plătiți cu cardul sau numerar.
**Sarcina utilizatorului.** *Cumpărați 2 bilete de „două călătorii” cu reducere de student și plătiți numerar cu o bancnotă de 10 lei.* Apoi, separat: *cumpărați cât mai repede un singur bilet de o călătorie, preț întreg.*
**Unde se folosește.** Laboratorul 03 – Legea lui Fitts și modelul KLM (lecția 03 din cursul dlui Pruteanu, *Modele și stiluri de interacțiune*).

## Cum deschideți variantele

Fiecare variantă este un singur fișier `index.html`, în folderele `1-nu-merge`, `2-merge`, `3-merge-bine`, `4-merge-foarte-bine`. Deschideți-l cu dublu-click sau, din VS Code, cu click dreapta → **Open with Live Server**.

## Ce aveți de făcut

1. Deschideți variantele **într-o ordine aleatorie**, fără să vă uitați la cod.
2. Realizați cele două sarcini în fiecare variantă. **Numărați** acțiunile (click-uri, apăsări de taste, mutări ale mâinii între mouse și tastatură) și cronometrați-vă. Notați și cât de departe și cât de mici sunt țintele pe care trebuie să le nimeriți.
3. Încercați și situații-limită: 0 bilete, 15 bilete, litere în loc de cifre, o sumă prea mică la plata numerar.
4. Completați tabelul și **ghiciți nivelul**; abia apoi apăsați butonul „Ce nivel are această interfață?”.

## Tabel de observație (de completat)

| Varianta | Ce funcționează | Ce încurcă | Euristica sau principiul încălcat | Nivelul ghicit |
|---|---|---|---|---|
| A (folderul …) | | | | |
| B (folderul …) | | | | |
| C (folderul …) | | | | |
| D (folderul …) | | | | |

Pentru KLM, adăugați o coloană cu numărul de operatori: **K** (tastă), **P** (indicare cu mouse-ul), **B** (click), **H** (mutarea mâinii), **M** (pregătire mentală).

## Exerciții

1. **Îmbunătățiți varianta 2 până la nivelul 3.** Cerințe concrete:
   - etichetele butoanelor radio se pot apăsa (fiecare `input` are un `<label for="…">`), ca ținta să fie tot rândul, nu doar cercul;
   - prețul se recalculează automat la orice schimbare, fără butonul „Calculează prețul” (un pas KLM mai puțin și fără preț „vechi” rămas pe ecran);
   - numărul de bilete se alege cu butoane − / + mari, limitat între 1 și 10, cu mesaj când se atinge limita;
   - afișați detaliat totalul (preț unitar, cantitate, reducere) cu unitatea „lei” și virgulă zecimală;
   - separați vizual „Cumpără” (buton principal, mare) de „Anulează” (secundar, mai departe), ca să nu fie apăsat din greșeală;
   - înlocuiți mesajele `alert()` („Invalid quantity”, „Error 12”) cu mesaje în pagină, în română, care spun ce trebuie făcut.
2. ★ **Refaceți varianta 1 de la zero**, fără ecrane succesive inutile și cu butonul „Următorul” acolo unde îl caută ochiul (după câmp, jos-dreapta), cu buton „Înapoi”.
3. ★ **Adăugați o funcționalitate la varianta 4**, de exemplu: bilet pentru bicicletă sau bagaj, o limită de timp cu avertizare („Sesiunea expiră în 30 s – continuați?”) sau un ecran în limba engleză.

> **Notă.** Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

## Ghid pentru cadrul didactic

- **Nivelul 1 – Nu merge.** Patru ecrane succesive fără „Înapoi”; legătura „Urmatorul” minusculă, în colțul opus câmpurilor (Fitts: distanță mare, țintă mică); coduri (`T2`, `AB1`, `R1`) explicate într-o notă de 9 px; totalul în bani, fără unitate (`1100`); litere în loc de cifre → `Total: NaN`; „Anulare” lângă „Plata”, identice, fără confirmare.
- **Nivelul 2 – Merge.** O singură pagină, dar: cercurile radio sunt singura țintă (fără `label`), prețul cere un pas suplimentar („Calculează”) și rămâne vechi dacă schimbați tipul după calcul, reducerea nu se vede în total, mesaje `alert()` tehnice, „Cumpără” și „Anulează” lipite și identice, lățime fixă.
- **Nivelul 3 – Merge bine.** Carduri mari pentru tip (cu tooltip despre valabilitate), categorii ca grup de butoane, numărător − / + cu limită și mesaj, rezumat cu prețul detaliat actualizat imediat, buton „Plătește X lei” mare, lângă total; plată în fereastră modală, cu validarea sumei și calculul restului; biletul afișat la final.
- **Nivelul 4 – Merge foarte bine.** În plus: „Cumpără acum” pentru biletul cel mai frecvent (KLM minim: două atingeri), „Repetă ultima comandă” (`localStorage`), butoane radio cu navigare din săgeți, tastele + și −, sume rapide la plata numerar, confirmare cu „Anulează și modifică”, `aria-live` pentru total, ținte mari (numărătorul are butoane de 56 px, cardurile cel puțin 88 px), mod întunecat cu contrast verificat.
