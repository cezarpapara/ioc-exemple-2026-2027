# Aplicația-exemplu 04 – Interfața operatorului de schimb valutar

**Ce face aplicația.** Ecranul de la ghișeul unei case de schimb: operatorul alege operațiunea și moneda, introduce suma, vede cursul aplicat și totalul în lei, apoi emite chitanța. Cursurile sunt demonstrative.
**Sarcina utilizatorului (operatorul).** *Un client vrea să cumpere 250 USD. Spuneți-i cât plătește și emiteți chitanța.* Apoi: *un alt client vinde 100,50 EUR* – observați ce se întâmplă.
**Unde se folosește.** Laboratorul 06 – Principii și ghiduri de proiectare: euristici, contrast, ținte (lecția 06 din cursul dlui Pruteanu); se poate relua la L07 (design vizual).

## Cum deschideți variantele

Fiecare variantă este un singur fișier `index.html`, în folderele `1-nu-merge`, `2-merge`, `3-merge-bine`, `4-merge-foarte-bine`. Deschideți-l cu dublu-click sau, din VS Code, cu click dreapta → **Open with Live Server**.

## Ce aveți de făcut

1. Deschideți variantele **într-o ordine aleatorie**, fără să vă uitați la cod.
2. Realizați sarcinile în fiecare variantă. Puneți-vă în locul operatorului, care face sute de operațiuni pe zi: unde poate greși? Ce greșeală l-ar costa bani?
3. Verificați contrastul textului cu [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) (culorile le aflați cu **F12 → Inspect**).
4. Pentru fiecare problemă găsită, numiți euristica Nielsen încălcată (de exemplu: vizibilitatea stării sistemului, potrivirea cu lumea reală, consecvența, prevenirea erorilor, recunoașterea în locul reamintirii).
5. Completați tabelul și **ghiciți nivelul**; abia apoi apăsați butonul „Ce nivel are această interfață?”.

## Tabel de observație (de completat)

| Varianta | Ce funcționează | Ce încurcă | Euristica sau principiul încălcat | Nivelul ghicit |
|---|---|---|---|---|
| A (folderul …) | | | | |
| B (folderul …) | | | | |
| C (folderul …) | | | | |
| D (folderul …) | | | | |

## Exerciții

1. **Îmbunătățiți varianta 2 până la nivelul 3.** Cerințe concrete:
   - redenumiți operațiunile din punctul de vedere al clientului („Clientul cumpără valută” / „Clientul vinde valută”) și afișați sub ele ce dă și ce primește clientul;
   - calculați totalul automat la fiecare modificare și afișați lângă el cursul aplicat („1 USD = 4,4900 lei”);
   - folosiți peste tot același format al numerelor (virgulă zecimală, „lei”), inclusiv pe chitanță;
   - înlocuiți `alert('Invalid amount')` cu un mesaj sub câmp, care explică ce sumă se acceptă;
   - chitanța apare într-o fereastră modală sau imediat sub buton, nu cu 300 px mai jos, iar după emitere se afișează un mesaj de succes;
   - înlocuiți antetele verde/roșu saturate (text alb pe verde deschis) cu culori cu contrast de cel puțin 4,5:1.
2. ★ **Refaceți varianta 1 de la zero**, cu text lizibil (fără roșu pe verde), etichete complete („Cumpărare”, nu „C”), rotunjire la două zecimale și chitanță care nu se poate emite fără calcul.
3. ★ **Adăugați o funcționalitate la varianta 4**, de exemplu: comision configurabil, conversia directă între două valute (EUR → USD) sau calculul invers („clientul are 500 de lei – câți euro primește?”).

> **Notă.** Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

## Ghid pentru cadrul didactic

- **Nivelul 1 – Nu merge.** Text roșu pe verde (contrast în jur de 1,5:1, iar culorile poartă semnificație); antete „C”/„V” și operațiuni „CUMP”/„VANZ” ambigue (cine cumpără?); `100,50` devine tacit `100` (`parseFloat`); rezultatul are zgomot de virgulă mobilă (`14.850000000000001`), fără unitate; „Chit.” emite chitanța și fără calcul (`TOTAL RON undefined`); butoane de 9 px, „Chit.” lipit de „Del”.
- **Nivelul 2 – Merge.** Operațiunile sunt numite din perspectiva casei, fără explicație; totalul cere „Calculează” și rămâne vechi dacă schimbați moneda; formate amestecate (`4.9500`, `898,00 RON`, `898.00 RON`); `alert()` în engleză; antete albe pe verde și roșu saturate; chitanța apare mult mai jos, fără niciun mesaj; lățime fixă de 960 px.
- **Nivelul 3 – Merge bine.** Operațiuni formulate pentru client și explicate, moneda cu denumire completă, sufixul valutei lângă sumă, calcul imediat cu cursul aplicat, rândul monedei și cursul folosit evidențiate în tabel, tooltips pe „Cumpărare”/„Vânzare”, validare (pozitivă, întreagă, maximum 10.000), chitanță în fereastră modală cu „Tipărește”, mesaj de succes.
- **Nivelul 4 – Merge foarte bine.** În plus: pas de verificare înainte de emitere, cu „Anulează, modific datele” (prevenirea erorilor costisitoare); numele clientului devine obligatoriu peste un prag, cu butonul care spune ce lipsește; sume rapide; istoricul ultimelor chitanțe (`localStorage`); `aria-live` pentru rezultat; Enter pentru emitere; focus vizibil; tipărirea doar a chitanței (`@media print`); mod întunecat.
