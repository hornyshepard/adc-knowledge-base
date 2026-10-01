---
id: DIG-054
title: Setările de calitate decid dacă impresiile plătite contează — brand safety, vizibilitate (viewability) și plafonul de frecvență
type: zettel
kind: checklist
skill: digital-marketing
also: [advertising-strategy, brand-strategy]
level: 2
tags: [brand-safety, viewability, frequency-capping, ad-server, whitelist, blacklist]
sources:
  - SRC-032 | cap. 2.3.4.2, p. 78-79; cap. 5.1.1.2, p. 161; cap. 5.2.1, p. 172; cap. 5.2.3, p. 174-177
status: growing
---

# Setările de calitate decid dacă impresiile plătite contează — brand safety, vizibilitate (viewability) și plafonul de frecvență

> **Ideea în o frază:** o impresie difuzată lângă conținut toxic, nevăzută sau repetată de prea multe ori costă bani și poate costa și reputație.

## Explicație

**Brand safety**: certitudinea că reclama apare doar într-un mediu compatibil cu brandul. Autorii citează opt categorii problematice (Integral Ad Science): conținut pentru adulți, alcool, discurs de ură, descărcări ilegale, droguri ilegale, limbaj ofensator, știri controversate, violență. Unelte: liste albe (*whitelists*, doar site-uri verificate), liste negre (*blacklists*), filtre pe categorii și servicii de tipul DoubleVerify, care analizează semantic paginile. În programmatic au existat cazuri de reclame difuzate în contexte rasiste sau sexuale.

**Vizibilitatea** (*viewability*): standardul MRC consideră o reclamă display văzută dacă cel puțin 50% din pixeli sunt pe ecran o secundă continuu; pentru video, 50% timp de două secunde consecutive. Atenție: în capitolul 5 aceeași carte dă un criteriu mai strict (peste 2 secunde și cel puțin 80% vizibil), deci standardul trebuie scris în contract. Mediile pot induce în eroare: uită-te la distribuție, câți au văzut sub o secundă și câți până la capăt.

**Plafonul de frecvență** (*frequency capping*): numărul maxim de expuneri pe utilizator. Ca să funcționeze, trebuie măsurate toate touchpoint-urile plătite, inclusiv TV și radio digital. Fără un ad server central, fiecare publisher își numără separat utilizatorii „unici", suprapunerile nu se văd, frecvența e subestimată și costurile cresc. Plafonarea se baza pe cookie-uri terțe; acum se fac soluții de identitate (e-mailuri criptate, ID-uri de dispozitiv).

## Aplicare

- Înainte de lansare: lista de excludere, standardul de vizibilitate, plafonul de frecvență pe utilizator și pe perioadă.
- Cere rapoarte pe aceste trei dimensiuni, nu doar impresii și clicuri.
- Pentru clienții cu multe campanii pe an, ia în calcul un ad server propriu: raportare centralizată, reach real fără suprapuneri, date care rămân la client când schimbă agenția.

## Exemplu

În campania de awareness pentru software-ul de video cu AI, firma își fixează o limită de patru expuneri pe persoană. Fără deduplicare între site-uri, aceeași persoană ar fi putut primi mult mai multe, fiecare plătită separat.

## Întrebări

- O listă albă foarte strictă reduce riscul, dar și reach-ul. Cum găsești echilibrul?

## Legături

- **vezi** [[DIG-055-frauda-publicitara-se-depisteaza-in-timpul-campaniei-prin|DIG-055]] — frauda, a patra setare de calitate.
- **vezi** [[DIG-059-targetarea-contextuala-pune-reclama-langa-subiectul-deja|DIG-059]] — brand safety în targetarea contextuală.
- **vezi** [[DIG-050-publicitatea-programatica-cumpara-fiecare-afisare-automat|DIG-050]] — automatizarea programatică face aceste setări obligatorii.
- **vezi** [[ADV-054-planul-media-se-judeca-dupa-acoperirea-la-frecventa-minima|ADV-054]] — planul media se judecă după acoperirea la frecvența minimă efectivă.
- **vezi** [[ADV-085-eficienta-publicitatii-digitale-ramane-nedovedita-iar|ADV-085]] — vizibilitatea slabă și frauda, motivele pentru care Percy și Rosenbaum-Elliott văd eficiența digitală ca nedovedită.
- **vezi** [[ADV-076-bugetul-de-comunicare-se-construieste-din-obiective-si|ADV-076]] — frecvența e „presiunea publicitară” din calculul bugetului.

## Surse

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 2.3.4.2 (p. 78–79), 5.1.1.2 (p. 161), 5.2.1 (p. 172), 5.2.3 (p. 174–177)

<!-- backlinks:start -->
## Backlinks

- [[ADV-054-planul-media-se-judeca-dupa-acoperirea-la-frecventa-minima|ADV-054]] _vezi_ — Planul media se judecă după acoperirea la frecvența minimă efectivă, nu după GRP-uri sau frecvența medie, iar în dubiu e mai bine să alegi frecvența
- [[DIG-047-pe-mobil-o-reclama-are-mai-putin-de-o-secunda-ca-sa-fie|DIG-047]] _vezi_ — Pe mobil, o reclamă are mai puțin de o secundă ca să fie văzută — fețe, contrast și emoție instantanee
- [[DIG-050-publicitatea-programatica-cumpara-fiecare-afisare-automat|DIG-050]] _vezi_ — Publicitatea programatică cumpără fiecare afișare automat, prin licitație în timp real — câștigă eficiență, dar cere date, bugete mari și control asupra plasării
- [[DIG-055-frauda-publicitara-se-depisteaza-in-timpul-campaniei-prin|DIG-055]] _vezi_ — Frauda publicitară se depistează în timpul campaniei, prin anomalii, nu după, iar plata pe vânzări verificate o face neatractivă
- [[DIG-059-targetarea-contextuala-pune-reclama-langa-subiectul-deja|DIG-059]] _vezi_ — Targetarea contextuală pune reclama lângă subiectul deja prezent în mintea cititorului, iar versiunea semantică citește și sentimentul contextului
- [[DIG-064-identitatea-fara-cookie-uri-are-trei-trepte-de-reach|DIG-064]] _vezi_ — Identitatea fără cookie-uri are trei trepte de reach — canalele proprii sau o singură „grădină închisă", camerele curate de date (data clean rooms) și ID-urile universale
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
