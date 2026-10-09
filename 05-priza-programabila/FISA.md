# Aplicația-exemplu 05 – Priză programabilă

**Ce face aplicația.** Simulează aplicația unei prize inteligente la care este conectată o aerotermă: o porniți și o opriți manual și îi stabiliți un program săptămânal (ora de pornire, ora de oprire, zilele).
**Sarcina utilizatorului.** *Adăugați un program pentru weekend (sâmbătă și duminică, 09:00–13:00), apoi porniți priza manual și aflați când se va opri singură. La final, ștergeți intervalul de weekend.*
**Unde se folosește.** Laboratorul 02 – Factorul uman (lecția 02 din cursul dlui Pruteanu): încărcarea cognitivă, memoria de scurtă durată, modelul mental al utilizatorului. Se poate relua la L06 (principii și ghiduri de proiectare).

## Cum deschideți variantele

Fiecare variantă este un singur fișier `index.html`, în folderele `1-nu-merge`, `2-merge`, `3-merge-bine`, `4-merge-foarte-bine`. Deschideți-l cu dublu-click (se deschide în browser) sau, din VS Code, cu click dreapta → **Open with Live Server**. Nu este nevoie de instalări (variantele 3 și 4 încarcă Bootstrap de pe internet).

## Ce aveți de făcut

1. Deschideți cele patru variante **într-o ordine aleatorie** (de exemplu 2, 4, 1, 3), fără să vă uitați întâi la cod.
2. Realizați sarcina de mai sus în fiecare variantă. Încercați și câteva greșeli firești: o oră de oprire mai mică decât cea de pornire, niciun buton de zi bifat, ștergerea din greșeală a unui interval.
3. Pentru fiecare variantă, răspundeți la întrebarea: *ce trebuie să țin minte ca să folosesc aplicația?* (coduri, formate, semnificația literelor). Aceasta este încărcarea cognitivă.
4. Deschideți fiecare variantă și la lățimea unui telefon (în browser: **F12 → Toggle device toolbar**, 375 px).
5. Notați în tabel ce funcționează, ce vă încurcă și ce principiu de la curs este încălcat. **Ghiciți nivelul** (1–4).
6. Abia apoi apăsați butonul „Ce nivel are această interfață?” din colțul paginii și comparați cu ce ați ghicit.

## Tabel de observație (de completat)

| Varianta | Ce funcționează | Ce încurcă | Euristica sau principiul încălcat | Nivelul ghicit |
|---|---|---|---|---|
| A (folderul …) | | | | |
| B (folderul …) | | | | |
| C (folderul …) | | | | |
| D (folderul …) | | | | |

Întrebări ajutătoare: Știu în fiecare moment dacă priza este pornită? Înțeleg de ce s-a pornit sau s-a oprit singură? Trebuie să rețin un format (de exemplu `0730` sau `1111100`)? Ce înseamnă „M” – marți sau miercuri? Pot anula o ștergere?

## Exerciții

1. **Îmbunătățiți varianta 2 până la nivelul 3.** Cerințe concrete:
   - afișați starea în română, cu text și cu un indicator vizual („Priza este pornită”), nu „Status: ON”;
   - înlocuiți literele de zile `L M M J V S D` cu `Lu Ma Mi Jo Vi Sâ Du` și adăugați fiecărei zile un tooltip cu numele complet;
   - înlocuiți `alert('Invalid input')` și `alert('Error 42: days = 0')` cu mesaje afișate lângă câmpul greșit, care spun ce trebuie corectat;
   - afișați zilele cu nume („Luni–Vineri”, „Sâmbătă, Duminică”), nu cu numere, și confirmați printr-un mesaj că intervalul a fost adăugat;
   - cereți confirmare înainte de ștergere și afișați „Următoarea acțiune programată”, ca utilizatorul să înțeleagă de ce priza se pornește sau se oprește singură;
   - eliminați lățimea fixă de 880 px, ca pagina să se adapteze pe telefon (Bootstrap: `container`, `row`, `col-md-…`).
2. ★ **Refaceți varianta 1 de la zero**, păstrând cele patru „sloturi” de program, dar cu câmpuri de tip `time`, zile alese prin butoane, mesaje clare în locul codului `E3`, confirmare înainte de „CLR” și un buton de pornire care funcționează sau explică de ce nu funcționează.
3. ★ **Adăugați o funcționalitate la varianta 4**, de exemplu: un mod „Concediu” care suspendă programul până la o dată aleasă, consumul estimat pe săptămână (kWh și lei) pentru programul curent sau copierea unui interval pe alte zile.

> **Notă.** Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

## Ghid pentru cadrul didactic

- **Nivelul 1 – Nu merge.** Text gri de 10–11 px pe alb, LED de 6 px aproape invizibil; butonul `ON/OFF` nu face nimic în modul implicit `AUTO` (fără niciun mesaj); programul cere formate de memorat (`HHMM`, zilele ca șir `1111100`), iar orice abatere afișează doar `E3`; un program nou suprascrie fără avertisment slotul ales; `CLR` șterge tot, fără confirmare; fără `viewport`. Principii: recunoaștere în loc de reamintire, încărcare cognitivă (Miller), vizibilitatea stării, potrivirea cu lumea reală, prevenirea erorilor, contrast.
- **Nivelul 2 – Merge.** Sarcina se poate realiza, dar: starea apare ca `Status: ON`, zilele `L M M J V S D` sunt ambigue (două „M”, fără tooltip), mesaje `alert()` tehnice (`Invalid input`, `Error 42`), tabel cu antet în engleză și zile ca numere (`1,2`), nicio confirmare la adăugare, ștergere directă dintr-un link mic, butoane cu stiluri diferite; programul suprascrie la fiecare 30 s starea aleasă manual, fără explicație (modelul mental al utilizatorului nu se potrivește cu sistemul); lățime fixă.
- **Nivelul 3 – Merge bine.** Indicator mare de stare (pictogramă și text), comutator, „Următoarea acțiune programată”, mesaj care explică până când rămâne valabilă comanda manuală, câmpuri cu etichete și valori implicite, zile `Lu…Du` cu tooltips, alegere rapidă (Luni–Vineri, Weekend, Zilnic), validare lângă câmp, mesaje de succes și informare, confirmare la ștergere, aranjare responsivă.
- **Nivelul 4 – Merge foarte bine.** În plus: programe peste noapte („a doua zi”), prevenirea suprapunerilor (mesajul numește intervalul existent), focus mutat pe câmpul greșit, ștergere cu „Anulează” în locul confirmării, axa „Astăzi” (0–24 h) cu ora curentă și text alternativ, `aria-live`, `fieldset`/`legend`, focus vizibil, contrast AA și în modul întunecat (care urmează setarea sistemului), programul păstrat în `localStorage`.
