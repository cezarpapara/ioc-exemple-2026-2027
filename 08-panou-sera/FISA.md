# Aplicația-exemplu 08 – Panou HMI pentru o seră

**Ce face aplicația.** Panoul operatorului unei sere (interfață om-mașină, HMI): temperatura aerului, umiditatea aerului și a solului, alarme, comenzi (ventilație, încălzire, irigare) și un grafic. Datele sunt simulate: soarele încălzește sera, ventilația o răcește, solul se usucă în timp.
**Sarcina utilizatorului.** *Supravegheați sera timp de două minute. Când apare o alarmă, aflați ce parametru a depășit ce limită, luați măsura potrivită (de exemplu porniți ventilația) și confirmați alarma. Porniți apoi irigarea pentru un minut.*
**Unde se folosește.** Laboratorul 12 – Panou de monitorizare (HMI) (lecțiile 14B – Vizualizarea informației și 15B – Interfețe om-mașină industriale din cursul dlui Pruteanu).

## Cum deschideți variantele

Fiecare variantă este un singur fișier `index.html`, în folderele `1-nu-merge`, `2-merge`, `3-merge-bine`, `4-merge-foarte-bine`. Deschideți-l cu dublu-click sau, din VS Code, cu click dreapta → **Open with Live Server**. Nu este nevoie de instalări (variantele 3 și 4 încarcă Bootstrap și Chart.js de pe internet; fără internet, varianta 4 explică de ce lipsește graficul).

## Ce aveți de făcut

1. Deschideți cele patru variante **într-o ordine aleatorie** și realizați sarcina în fiecare.
2. **Testul de la distanță:** îndepărtați-vă la 2–3 metri de ecran. Puteți citi valorile? Vă dați seama dacă e totul în regulă?
3. **Testul fără culori:** priviți panoul în tonuri de gri (în Chrome: **F12 → ⋮ → More tools → Rendering → Emulate vision deficiencies → Achromatopsia**). Mai recunoașteți alarmele?
4. Numărați câte mesaje produce o singură alarmă care durează un minut. Puteți confirma că ați văzut-o?
5. Completați tabelul și **ghiciți nivelul** (1–4). Abia apoi apăsați butonul „Ce nivel are această interfață?”.

## Tabel de observație (de completat)

| Varianta | Ce funcționează | Ce încurcă | Euristica sau principiul încălcat | Nivelul ghicit |
|---|---|---|---|---|
| A (folderul …) | | | | |
| B (folderul …) | | | | |
| C (folderul …) | | | | |
| D (folderul …) | | | | |

Întrebări ajutătoare: Ce element este cel mai mare pe ecran și este el cel mai important? Știu dacă ventilația este pornită acum? Graficul are axe și unități? Alarma spune ce s-a întâmplat, când și ce trebuie făcut? Pot porni irigarea din greșeală?

## Exerciții

1. **Îmbunătățiți varianta 2 până la nivelul 3.** Cerințe concrete:
   - măriți valorile (cel mai mare text de pe ecran) și puneți sub fiecare intervalul normal;
   - afișați pentru fiecare senzor o stare cu **text și simbol**, nu doar culoare (● Normal, ▲ Atenție, ■ Alarmă), și un mesaj general care spune **ce** parametru este în alarmă;
   - înlocuiți perechile „ON”/„OFF” cu un comutator care arată starea curentă („Ventilație: pornită”);
   - cereți confirmare la pornirea irigării și afișați timpul rămas;
   - înregistrați alarma **o singură dată**, la apariție, cu ora (HH:MM:SS) și un mesaj în română, și adăugați butonul „Confirmă”;
   - înlocuiți graficul desenat manual cu unul Chart.js, cu axe, unități și legendă.
2. ★ **Refaceți varianta 1 de la zero**, cu denumiri clare în locul codurilor `T1`, `H1`, `S1`, umiditatea solului în procente, valori cu o zecimală actualizate la 2 secunde și butoane de comandă cu text și stare vizibilă.
3. ★ **Adăugați o funcționalitate la varianta 4**, de exemplu: limite configurabile (cu validare), exportul jurnalului de alarme în CSV sau un mod automat care pornește ventilația peste 28 °C (cu anunțarea fiecărei acțiuni automate).

> **Notă.** Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

## Ghid pentru cadrul didactic

- **Nivelul 1 – Nu merge.** Gri pe gri, text de 9–11 px; coduri `T1`, `H1`, `S1` fără unități; umiditatea solului ca valoare brută ADC (≈600); valori cu două zecimale, actualizate de două ori pe secundă (cifrele „fug”); alarma este doar o celulă roșie cu text roșu (ilizibilă și dependentă de culoare); butoane `V`, `I`, `H` de 9 px, fără stare vizibilă; irigarea pornește fără confirmare; în loc de grafic, un șir de numere care crește la nesfârșit. Principii: vizibilitatea stării, potrivirea cu lumea reală, ierarhie vizuală, culoarea ca unic purtător de informație (WCAG 1.4.1), prevenirea erorilor.
- **Nivelul 2 – Merge.** Valorile au unități, dar au aceeași mărime ca etichetele; „ALARM!” generic, în engleză, fără parametru; perechi de butoane „ON” (verde) / „OFF” (roșu) fără starea curentă; irigarea pornește direct, fără durată afișată; grafic fără axe, unități și legendă, cu scară care se schimbă continuu (variațiile mici par dramatice); jurnal cu coduri și milisecunde (`ERR_T_HIGH 1791482559380`), o linie nouă la fiecare 2 s cât timp durează alarma (*alarm flood*), fără confirmare; câmpuri goale în primele secunde; lățime fixă de 1100 px.
- **Nivelul 3 – Merge bine.** Bandă de stare generală (text, simbol și culoare), carduri cu valoare mare, unitate, insignă de stare, interval normal și praguri de alarmă scrise, bordură colorată; tooltips care descriu senzorii; comutatoare cu starea în text; irigare cu confirmare, timp rămas și buton de oprire; grafic Chart.js cu două axe titrate și legendă (ultimele 2 minute); jurnal cu o singură intrare la agravarea stării (ora, parametru, valoare și prag) și buton „Confirmă”; aranjare responsivă.
- **Nivelul 4 – Merge foarte bine.** În plus: histerezis (o alarmă dispare abia când valoarea revine cu 0,5 în interval, deci nu „pâlpâie”); tendința fiecărei valori (↑ crește, ↓ scade, → stabil); limitele de temperatură ca linii întrerupte pe grafic; mesaj care sugerează acțiunea („Porniți ventilația”); `aria-live="assertive"` pentru alarme noi; contor „N alarme neconfirmate” și „Confirmă toate”; atenția are chenar întrerupt, alarma chenar plin (formă, nu doar culoare); irigarea este refuzată, cu explicație, când solul este deja umed, iar confirmarea arată valoarea curentă și o bară de progres; panoul funcționează și fără Chart.js (mesaj explicativ); mod întunecat ales de operator, aplicat și graficului; tabelul de alarme se rearanjează pe telefon.
