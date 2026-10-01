---
id: DIG-1029
title: Publicitatea programatică cumpără fiecare impresie automat, prin licitație în timp real — câștigă eficiență, pierde control și are nevoie de date și bugete mari
type: zettel
kind: concept
skill: digital-marketing
also: [advertising-strategy]
level: 2
tags: [programmatic, rtb, dsp, dmp, ad-server, ctv, context-matching]
sources:
  - SRC-032 | cap. 2.3.4.1, p. 76-77; cap. 5.1, p. 159-171
status: seed
---

# Publicitatea programatică cumpără fiecare impresie automat, prin licitație în timp real — câștigă eficiență, pierde control și are nevoie de date și bugete mari

> **Ideea în o frază:** programmatic-ul înlocuiește negocierea manuală a spațiului cu algoritmi care decid în milisecunde, pentru fiecare afișare, dacă și cu cât cumpără.

## Explicație

**De la ad server la programmatic.** La început, bannerele se inserau manual în codul fiecărei pagini. Ad serverul a rezolvat problema: publisherul pune pe pagină un mic script (*ad server tag*), iar reclama e livrată, numărată și optimizată automat. Publisherii s-au grupat apoi în rețele de reclame. Algoritmii au automatizat treptat tot procesul: în 2022, aproximativ 87% din publicitatea display globală era cumpărată programmatic (PwC/IAB).

**Licitația în timp real** (*real-time bidding*, RTB): advertiserul fixează CPM-ul maxim, publisherul prețul minim, iar sistemul decide în milisecunde dacă reclama se afișează. Dacă nu există destul inventar la prețul oferit, advertiserul trebuie să crească oferta. Datele vin dintr-un DMP, care integrează date first-, second- și third-party, iar un instrument de bannere dinamice poate adapta creația fiecărui profil. Plata se poate lega de orice KPI măsurabil: produse vândute, instalări, abonări la newsletter, test drive-uri. Programmatic-ul se extinde și la TV conectat.

**Critici:**

- e eficient doar cu multe date și bugete mari, de ordinul a cinci-șase cifre (Lammenett), deci nu e potrivit pentru bugete mici;
- optimizează spre CTR și impresii, deși mediul în care apare reclama contează mult (*context matching*), așa că listele de site-uri trebuie verificate;
- automatizarea aduce o pierdere de control.

## Aplicare

- Înainte de a recomanda programmatic, verifică bugetul și volumul de date ale clientului.
- Cere lista de site-uri și setările de brand safety și fraudă, nu doar CPM-ul obținut.
- Definește tu obiectivele și KPI-urile: spre deosebire de Meta sau Google, programmatic-ul nu le propune implicit.

## Exemplu

Capitolul 5 construiește un caz complet pentru un magazin de mobilă: date imobiliare într-un DMP, un DSP pentru reach și bannere dinamice care schimbă bucătăria și prețul după profil.

## Întrebări

- Dacă o mașină alege unde apare reclama, cine răspunde pentru plasare?

## Legături

- **vezi** [[DIG-1027-brand-safety-viewability-si-plafonul-de-frecventa|DIG-1027]] — setările de calitate obligatorii în programmatic.
- **vezi** [[DIG-1030-cazul-bucatariilor-dmp-dsp-si-bannere-dinamice|DIG-1030]] — cazul bucătăriilor, programmatic de la cap la coadă.
- **vezi** [[DIG-1023-identitatea-fara-cookie-uri-trei-trepte-de-reach|DIG-1023]] — identitatea de care depinde targetarea programatică după cookie-uri.
- **vezi** [[DIG-1021-strategia-first-party-incepe-cu-intrebarea-de-vanzari|DIG-1021]] — tipurile de date care alimentează DMP-ul.

## Surse

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 2.3.4.1 (p. 76–77) și 5.1 (p. 159–171)

<!-- backlinks:start -->
## Backlinks

- [[DIG-1023-identitatea-fara-cookie-uri-trei-trepte-de-reach|DIG-1023]] _vezi_ — Identitatea fără cookie-uri are trei trepte de reach — canalele proprii sau o singură „grădină închisă", camerele curate de date (data clean rooms) și ID-urile universale
- [[DIG-1027-brand-safety-viewability-si-plafonul-de-frecventa|DIG-1027]] _vezi_ — Setările de calitate decid dacă impresiile plătite contează — brand safety, vizibilitate (viewability) și plafonul de frecvență
- [[DIG-1028-frauda-publicitara-se-depisteaza-in-timpul-campaniei|DIG-1028]] _vezi_ — Frauda publicitară se depistează în timpul campaniei, prin anomalii, nu după, iar plata pe vânzări verificate o face neatractivă
- [[DIG-1030-cazul-bucatariilor-dmp-dsp-si-bannere-dinamice|DIG-1030]] _exemplu_ — Cazul bucătăriilor — date imobiliare anonimizate, un DMP, un DSP și bannere dinamice transformă un pliant pentru toată lumea într-o ofertă pentru fiecare gospodărie
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
