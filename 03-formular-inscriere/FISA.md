# Aplicația-exemplu 03 – Formular de înscriere la un atelier

**Ce face aplicația.** Un formular de înscriere la un atelier (nume, e-mail, telefon, specializare, an, sesiune, observații, acord). Datele nu se trimit nicăieri: totul rulează în browser.
**Sarcina utilizatorului.** *Înscrieți-vă în sesiunea de după-amiază; dacă nu se poate, în cea de dimineață.* Introduceți întâi intenționat un e-mail fără domeniu (`ana@exemplu`) și un telefon scris cu spații (`0722 123 456`), apoi corectați ce vi se cere.
**Unde se folosește.** Laboratorul 08 – Feedback, erori și controlul utilizatorului; Laboratorul 10 – Accesibilitate și design universal (lecțiile 08 și 10 din cursul dlui Pruteanu).

## Cum deschideți variantele

Fiecare variantă este un singur fișier `index.html`, în folderele `1-nu-merge`, `2-merge`, `3-merge-bine`, `4-merge-foarte-bine`. Deschideți-l cu dublu-click sau, din VS Code, cu click dreapta → **Open with Live Server**.

## Ce aveți de făcut

1. Deschideți variantele **într-o ordine aleatorie**, fără să vă uitați la cod.
2. Realizați sarcina în fiecare variantă. Notați: aflați **ce** este greșit și **unde**? Vi se păstrează datele după o eroare? Mesajele sunt în limba voastră și vă spun ce să faceți?
3. Testați **doar cu tastatura** (Tab, Shift+Tab, Space, Enter): ajungeți la toate câmpurile? Vedeți mereu unde este focusul?
4. Măriți textul paginii (Ctrl + +) la 200% și deschideți pagina la lățimea unui telefon.
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
   - legați fiecare etichetă de câmpul ei (`<label for="email">`) și marcați consecvent câmpurile obligatorii (`*` peste tot, cu explicația lui deasupra formularului);
   - telefonul devine opțional și acceptă spații (`0722 123 456`); explicați de ce îl cereți;
   - înlocuiți seria de `alert()`-uri cu mesaje sub fiecare câmp, în română, care spun ce să facă utilizatorul (de exemplu „Adresa pare incompletă. Exemplu corect: ana.popescu@exemplu.ro”);
   - sesiunea plină se dezactivează din start, cu textul „Complet”, în loc să afle utilizatorul abia la trimitere;
   - la succes afișați un mesaj în pagină cu sesiunea aleasă și adresa la care vine confirmarea; scoateți butonul „Reset” de lângă „Submit”;
   - folosiți Bootstrap (`form-control`, `row`, `col-md-6`) ca formularul să arate bine și pe telefon.
2. ★ **Refaceți varianta 1 de la zero**: etichete vizibile (nu doar `placeholder`), contrast suficient, datele nu se șterg la eroare, butonul de trimitere arată ca acțiunea principală.
3. ★ **Adăugați o funcționalitate la varianta 4**, de exemplu: lista de așteptare pentru sesiunea plină, alegerea unei a doua sesiuni sau un câmp „Cum ați aflat de atelier?” cu opțiunea „Altceva” care deschide un câmp text.

> **Notă.** Exemplele din acest repository sunt materiale de lucru: proiectul vostru trebuie să fie original; o variantă copiată sau ușor modificată nu se punctează.

## Ghid pentru cadrul didactic

- **Nivelul 1 – Nu merge.** Doar `placeholder` în loc de etichete (dispar la tastare, gri foarte deschis); nimic nu arată ce este obligatoriu; codurile `INFO`, `S1`, `S2` nu sunt explicate; telefonul cere un format nespus (`07xxxxxxxx`, fără spații); orice eroare produce același „Formular invalid!” mic și **golește tot formularul**; butonul mare și colorat este „Resetează”, iar „Trimite” pare dezactivat; succesul este un text gri, abia vizibil.
- **Nivelul 2 – Merge.** Etichete prezente, dar nelegate de câmpuri; asteriscuri inconsecvente; erorile apar pe rând, în `alert()`, cu mesaje tehnice în engleză („Error 42: phone format”); sesiunea plină se află abia la trimitere; „Success!” fără detalii, iar formularul rămâne completat; „Reset” lângă „Submit”; tabel de lățime fixă.
- **Nivelul 3 – Merge bine.** Etichete legate, explicația pentru `*`, texte de ajutor, tooltip „De ce cerem telefonul?”, validare la părăsirea câmpului și la trimitere, cu mesaje prietenoase și exemple; sesiunea plină dezactivată și marcată „Complet”; stare de încărcare la trimitere; confirmare cu rezumat; aranjare responsivă.
- **Nivelul 4 – Merge foarte bine.** În plus: sumarul erorilor în partea de sus, cu legături care duc focusul la câmp; `aria-invalid`, `aria-describedby`, `autocomplete`, `inputmode`; sugestie pentru greșelile de tastare ale domeniului (`gmial.com` → `gmail.com`); contor de caractere; ciornă salvată automat și restaurată; confirmare înainte de golire; sesiune preselectată (valoare implicită); focus vizibil; mod întunecat.
