# Aplicația-exemplu 01 – Automat de cafea

**Ce face aplicația.** Simulează ecranul tactil al unui automat de cafea: alegeți băutura și cantitatea de zahăr, plătiți cu monede, bancnote sau card și primiți băutura (și restul).
**Sarcina utilizatorului.** *Cumpărați un cappuccino cu puțin zahăr, plătiți cu o bancnotă de 10 lei și aflați cât rest primiți.*
**Unde se folosește.** Laboratorul 05 – Prototiparea interfețelor (lecția 05 din cursul dlui Pruteanu); se poate relua la L06 (euristici) și L08 (feedback și erori).

## Cum deschideți variantele

Fiecare variantă este un singur fișier `index.html`, în folderele `1-nu-merge`, `2-merge`, `3-merge-bine`, `4-merge-foarte-bine`. Deschideți-l cu dublu-click (se deschide în browser) sau, din VS Code, cu click dreapta → **Open with Live Server**. Nu este nevoie de instalări.

## Ce aveți de făcut

1. Deschideți cele patru variante **într-o ordine aleatorie** (de exemplu 3, 1, 4, 2), fără să vă uitați întâi la cod.
2. Realizați sarcina de mai sus în fiecare variantă. Încercați și câteva „greșeli” firești: apăsați „Preparează”/„OK” fără bani, alegeți o băutură indisponibilă, anulați după ce ați introdus bani.
3. Deschideți fiecare variantă și pe telefon (sau în browser: **F12 → Toggle device toolbar**, lățime 375 px).
4. Notați în tabel ce funcționează, ce vă încurcă și ce principiu de la curs este încălcat. **Ghiciți nivelul** (1–4).
5. Abia apoi apăsați butonul „Ce nivel are această interfață?” din colțul paginii și comparați cu ce ați ghicit.

## Tabel de observație (de completat)

| Varianta | Ce funcționează | Ce încurcă | Euristica sau principiul încălcat | Nivelul ghicit |
|---|---|---|---|---|
| A (folderul …) | | | | |
| B (folderul …) | | | | |
| C (folderul …) | | | | |
| D (folderul …) | | | | |

Întrebări ajutătoare: Știți în fiecare moment ce ați ales și cât credit aveți? Aflați de ce nu se întâmplă nimic când apăsați un buton? Puteți anula fără să pierdeți bani? Textul se citește ușor? Butoanele se nimeresc ușor cu degetul?

## Exerciții

1. **Îmbunătățiți varianta 2 până la nivelul 3.** Cerințe concrete:
   - butonul băuturii alese rămâne evidențiat (selecția este vizibilă), iar numele băuturii apare lângă butonul de comandă, nu ca număr („Produs: 2”) jos în pagină;
   - înlocuiți `alert()` cu un mesaj afișat în pagină, în limba română, care spune ce lipsește și cât mai trebuie plătit („Mai introduceți 2,00 lei”);
   - folosiți culorile consecvent: butonul principal „Comandă” într-o culoare neutră sau pozitivă, „Renunță” secundar (nu roșu pentru acțiunea principală și verde pentru renunțare);
   - afișați zahărul ales în confirmare și restul cu două zecimale („3,00 lei”);
   - dezactivați comanda până când există o băutură aleasă și o plată suficientă;
   - eliminați lățimea fixă de 900 px, ca pagina să se adapteze pe telefon (Bootstrap: `container`, `row`, `col-md-…`).
2. ★ **Refaceți varianta 1 de la zero**, păstrând ideea de tastatură cu coduri, dar cu etichete lizibile, contrast suficient, mesaje explicite în locul codurilor `E1`/`E3` și confirmare înainte ca „C” să șteargă creditul.
3. ★ **Adăugați o funcționalitate la varianta 4**, de exemplu: mărimea paharului (mic/mediu/mare, cu preț diferit), un buton „Ca data trecută” sau un mesaj care avertizează că automatul nu mai are monede pentru rest.

> **Notă.** Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

## Ghid pentru cadrul didactic

- **Nivelul 1 – Nu merge.** Băuturile se aleg prin coduri (`A3`), legenda este minusculă și cu contrast foarte slab; ținte de 22 px; zahărul apare criptic (`S3`); erorile sunt coduri (`E1`, `E3`) afișate o clipă; „C” șterge și creditul, fără confirmare; restul nu se dă, rămâne pe ecran ca număr; nu există `viewport`. Principii: vizibilitatea stării, potrivirea cu lumea reală, recunoaștere în loc de reamintire, prevenirea erorilor, contrast, mărimea țintelor (Fitts).
- **Nivelul 2 – Merge.** Sarcina se poate duce la capăt, dar: selecția nu se vede (apare „Produs: 2”, departe de butoane), mesaje `alert()` tehnice în engleză („Invalid input”), amestec de limbi și de diacritice, culori inversate (roșu pentru „Comandă”, verde pentru „Renunță”), zahărul nu apare în confirmare, restul fără unitate, lățime fixă de 900 px.
- **Nivelul 3 – Merge bine.** Pași numerotați, carduri cu preț și ingrediente (tooltip), selecție evidentă, rezumatul comenzii, mesaje de informare/avertizare/succes în pagină, buton dezactivat până la plata completă, bară de progres la preparare, anulare cu returnarea creditului, aranjare responsivă.
- **Nivelul 4 – Merge foarte bine.** În plus: opțiuni ca butoane radio (navigare cu săgețile, focus vizibil), `aria-live` pentru mesaje, monedele se dezactivează după acoperirea prețului (prevenire), confirmare la anulare (și tasta Esc), etapele preparării, preferința de zahăr și tema (luminoasă/întunecată) păstrate în `localStorage`, ținte de minimum 44 px, respectarea `prefers-reduced-motion`.
