# Aplicația-exemplu 07 – Meniu de restaurant cu coș de comandă

**Ce face aplicația.** Meniul online al unui bistro (fictiv): alegeți preparate, le puneți în coș, completați datele de livrare și trimiteți comanda. Variantele 1 și 2 conțin **tipare manipulative** (*dark patterns*) întâlnite des pe site-uri reale.
**Sarcina utilizatorului.** *Comandați o ciorbă de burtă și două porții de sarmale, cu livrare, fără tacâmuri și fără abonare la oferte. Înainte de a trimite, aflați exact cât plătiți.*
**Unde se folosește.** Laboratorul 07 – Designul vizual (ierarhie, tipografie, culoare, contrast) și Laboratorul 11 – Design responsiv și etica proiectării (lecțiile 07, 11 și 13B din cursul dlui Pruteanu).

## Cum deschideți variantele

Fiecare variantă este un singur fișier `index.html`, în folderele `1-nu-merge`, `2-merge`, `3-merge-bine`, `4-merge-foarte-bine`. Deschideți-l cu dublu-click sau, din VS Code, cu click dreapta → **Open with Live Server**. Nu este nevoie de instalări (variantele 3 și 4 încarcă Bootstrap de pe internet).

## Ce aveți de făcut

1. Deschideți cele patru variante **într-o ordine aleatorie** și realizați sarcina în fiecare.
2. Notați **prețul pe care îl așteptați** înainte de a trimite comanda și **prețul final** afișat. Dacă diferă, aflați de unde vine diferența.
3. Căutați tiparele manipulative: opțiuni bifate dinainte, costuri care apar abia la final, numărători inverse, „doar 2 porții rămase”, butoane care vă fac să vă simțiți vinovați când refuzați („Nu, mulțumesc, nu vreau reduceri”). Pentru fiecare, scrieți **cui folosește** și **cui dăunează**.
4. Deschideți fiecare variantă la lățimea unui telefon (**F12 → Toggle device toolbar**, 375 px): se poate comanda fără derulare orizontală?
5. Completați tabelul și **ghiciți nivelul** (1–4). Abia apoi apăsați butonul „Ce nivel are această interfață?”.

## Tabel de observație (de completat)

| Varianta | Ce funcționează | Ce încurcă | Euristica sau principiul încălcat | Nivelul ghicit |
|---|---|---|---|---|
| A (folderul …) | | | | |
| B (folderul …) | | | | |
| C (folderul …) | | | | |
| D (folderul …) | | | | |

Întrebări ajutătoare: Prețurile au același format? Văd taxa de livrare înainte de final? Ce era bifat fără să bifez eu? Pot scoate un produs din coș sau schimba cantitatea? Textul se citește pe fundalul ales? Butonul principal se distinge de cel secundar?

## Exerciții

1. **Îmbunătățiți varianta 2 până la nivelul 3.** Cerințe concrete:
   - eliminați tiparele manipulative: banda cu numărătoarea inversă, mesajul „Doar 2 porții rămase”, opțiunile bifate dinainte și fereastra „Nu pleca fără desert!”;
   - afișați toate costurile (livrare, ambalare) în coș **de la început**, nu doar în rezumatul final, și bacșișul implicit 0;
   - adăugați butoane − și + pentru cantitate și afișați prețurile cu două zecimale și unitate („24,00 lei”);
   - puneți etichete `<label>` câmpurilor și înlocuiți `alert('Date invalide')` cu mesaje lângă câmpul greșit;
   - anunțați adăugarea în coș printr-un mesaj scurt (de exemplu un *toast* Bootstrap);
   - faceți pagina responsivă: meniul și coșul unul sub altul pe telefon (Bootstrap: `row`, `col-lg-8`, `col-lg-4`).
2. ★ **Refaceți varianta 1 de la zero**, cu un fundal și culori care respectă contrastul WCAG AA (verificați cu WebAIM Contrast Checker) și cu un coș în care se vede ce ați ales.
3. ★ **Adăugați o funcționalitate la varianta 4**, de exemplu: filtrarea preparatelor vegetariene, alegerea între livrare și ridicare personală sau o listă de alergeni pentru fiecare preparat.

> **Notă.** Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

## Ghid pentru cadrul didactic

- **Nivelul 1 – Nu merge.** Text roșu închis pe fundal roșu (contrast foarte slab), titlu cu font caligrafic, prețuri în cinci formate („24”, „19.00 RON”, „36,-”, „RON 26”); „[+]” minuscule; coșul este doar „Coș: 2”, fără listă, fără ștergere sau cantități; tacâmuri „premium” și desert bifate dinainte; numărătoare inversă falsă care reîncepe; câmpuri doar cu placeholder; telefonul cu spații este refuzat fără mesaj; fereastra „STAI! Nu pleca!” cu buton verde uriaș și refuz gri minuscul (*confirmshaming*), iar abonarea se face oricum; totalul apare abia la final și include o „taxă de serviciu” nemenționată (*drip pricing*); lățime fixă. Tipare: *preselection*, *sneaking*, *false urgency*, *confirmshaming*, *forced action*, *hidden costs*.
- **Nivelul 2 – Merge.** Comanda se poate trimite, coșul are listă și ștergere, dar: urgență falsă („Mai ai 09:59”, reîncepe la fiecare vizită), raritate falsă („Doar 2 porții rămase!”), tacâmuri și oferte prin SMS bifate dinainte, bacșiș 10% preselectat, fereastră de *confirmshaming* pentru desert (reducerea promisă nici nu se aplică), „Taxă ambalare și servire 7,99” afișată doar în rezumatul final, `alert('Date invalide')`, câmpuri fără etichete, fără cantități −/+, lățime fixă de 960 px.
- **Nivelul 3 – Merge bine.** Costul livrării și pragul de gratuitate sunt anunțate în antet; categorii; carduri cu prețuri uniforme și insigna „Vegetarian” (cu tooltip); mesaj la adăugarea în coș; coș cu −/+, subtotal, livrare și total vizibile permanent; opțiunile sunt nebifate și marcate „gratuit”/„opțional”; câmpuri cu etichete și validare (07xxxxxxxx); butonul arată totalul; mesaj de succes cu suma și timpul de livrare; pe telefon, coșul trece sub meniu, iar un buton fix „Vezi coșul (3) · 74,00 lei” duce la el.
- **Nivelul 4 – Merge foarte bine.** În plus: pas de verificare („Verifică comanda” → rezumat → „Confirm și trimit (… lei)” sau „Modific comanda”); mențiunea „Totalul afișat este cel final”; limite de 1–10 porții cu butoane dezactivate și mesaj; eliminare cu „Anulează”; coș păstrat în `localStorage`; mesaje `aria-live`, etichete ARIA care numesc preparatul; focus mutat logic (pe coș, pe primul câmp greșit, pe rezumat); `autocomplete` și `inputmode` pe câmpuri; mod întunecat după setarea sistemului; `prefers-reduced-motion`.
