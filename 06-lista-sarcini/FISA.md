# Aplicația-exemplu 06 – Listă de sarcini

**Ce face aplicația.** O listă de sarcini (*to-do list*): adăugați sarcini, le bifați când sunt gata, le ștergeți și filtrați lista (toate, active, finalizate).
**Sarcina utilizatorului.** *Adăugați sarcina „Pregătesc prezentarea proiectului”, marcați o sarcină ca finalizată, afișați doar sarcinile finalizate, apoi ștergeți una dintre ele.*
**Unde se folosește.** Laboratorul 09 – Testarea utilizabilității (lecția 09 din cursul dlui Pruteanu, Evaluarea utilizabilității): aplicația este „subiectul” unui mic test cu utilizatori, cu timp, erori și chestionarul SUS.

## Cum deschideți variantele

Fiecare variantă este un singur fișier `index.html`, în folderele `1-nu-merge`, `2-merge`, `3-merge-bine`, `4-merge-foarte-bine`. Deschideți-l cu dublu-click sau, din VS Code, cu click dreapta → **Open with Live Server**. Nu este nevoie de instalări (variantele 3 și 4 încarcă Bootstrap de pe internet).

## Ce aveți de făcut

1. Lucrați **în perechi**: unul este *utilizator*, celălalt *observator*. Schimbați rolurile după două variante.
2. Observatorul deschide variantele **într-o ordine aleatorie** și citește sarcina cu voce tare. Utilizatorul gândește cu voce tare (*think aloud*); observatorul nu ajută și nu explică.
3. Observatorul notează pentru fiecare variantă: timpul (în secunde), numărul de erori și de câte ori utilizatorul a cerut ajutor.
4. Completați împreună tabelul de observație și **ghiciți nivelul** (1–4).
5. Abia apoi apăsați butonul „Ce nivel are această interfață?” și comparați. ★ Opțional: completați chestionarul SUS pentru varianta cea mai slabă și pentru cea mai bună.

## Tabel de observație (de completat)

| Varianta | Ce funcționează | Ce încurcă | Euristica sau principiul încălcat | Nivelul ghicit |
|---|---|---|---|---|
| A (folderul …) | | | | |
| B (folderul …) | | | | |
| C (folderul …) | | | | |
| D (folderul …) | | | | |

Măsurători (observatorul): Varianta | Timp (s) | Erori | Ajutor cerut | Sarcina terminată (da/nu).

Întrebări ajutătoare: Funcționează tasta Enter? Se vede clar ce sarcină este finalizată și ce filtru este activ? Pot șterge din greșeală toată lista? Pot anula o ștergere? Ce se întâmplă dacă adaug un text gol sau aceeași sarcină de două ori?

## Exerciții

1. **Îmbunătățiți varianta 2 până la nivelul 3.** Cerințe concrete:
   - puneți câmpul într-un `<form>`, cu etichetă `<label>`, ca sarcina să se adauge și cu tasta Enter;
   - înlocuiți `alert('Error: empty string')` cu un mesaj sub câmp („Scrieți sarcina, cel puțin 3 caractere”) și `alert('OK')` cu un mesaj care spune câte sarcini au fost șterse;
   - folosiți aceeași limbă peste tot („Adaugă”, „Finalizate”, nu „Add”, „Completed”) și evidențiați filtrul activ, cu numărul de sarcini („Active (2)”);
   - cereți confirmare înainte de ștergere și afișați un mesaj potrivit când lista filtrată este goală;
   - afișați textul sarcinii cu `textContent` (sau escapat), nu direct în `innerHTML`;
   - eliminați lățimea fixă de 720 px (Bootstrap: `container`, `list-group`).
2. ★ **Refaceți varianta 1 de la zero**, cu contrast suficient, etichetă vizibilă, butoane cu text („Adaugă”, „Șterge tot”) despărțite între ele și ștergere care nu se face prin dublu-click.
3. ★ **Adăugați o funcționalitate la varianta 4**, de exemplu: termen-limită cu evidențierea sarcinilor întârziate, sortare după prioritate sau reordonare prin tragere (cu alternativă din tastatură).

> **Notă.** Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

## Ghid pentru cadrul didactic

- **Nivelul 1 – Nu merge.** Text gri închis pe fundal aproape negru, font monospace mic; câmp fără etichetă (`...`); Enter nu face nimic; „+” adaugă și texte goale și nu golește câmpul (apar dubluri); „-”, lipit de „+”, șterge toată lista fără confirmare; click pe text bifează (diferență de nuanță abia vizibilă), dublu-click șterge (nedescoperibil); filtrul „Inactive” este ambiguu și revine singur la „Toate”. Principii: vizibilitatea stării, prevenirea erorilor, controlul utilizatorului (fără anulare), legea lui Fitts (ținte mici și periculos de apropiate), contrast.
- **Nivelul 2 – Merge.** Sarcina se realizează, dar: Enter nu funcționează, `alert()` tehnice (`Error: empty string`, `OK`), amestec de limbi („Add”, „Completed”, „Șterge finalizate”), filtrul activ nu se vede și nu are contoare, „X” șterge imediat, dublurile sunt permise, textul ajunge direct în `innerHTML`, lățime fixă de 720 px.
- **Nivelul 3 – Merge bine.** Formular cu etichetă și Enter, validare lângă câmp, prioritate cu insignă text, mesaje de succes și informare care numesc sarcina, rezumat („3 active, 1 finalizate”), filtre cu contoare și stare activă, mesaje pentru liste goale, ștergere cu confirmare, „Șterge finalizatele” dezactivat când nu are ce șterge, aranjare responsivă.
- **Nivelul 4 – Merge foarte bine.** În plus: lista și filtrul păstrate în `localStorage`; tasta `/` mută cursorul în câmp, Esc îl golește; contor 0/80; dublurile sunt refuzate; sarcina nouă apare sus, evidențiată; editare pe loc (Enter salvează, Esc renunță); ștergere fără confirmare, dar cu „Anulează”; focusul trece la sarcina următoare după ștergere; `aria-live`, `aria-pressed`, etichete care numesc sarcina; mod întunecat ales de utilizator, cu contrast AA; acordul corect al numeralului („20 de sarcini”).
