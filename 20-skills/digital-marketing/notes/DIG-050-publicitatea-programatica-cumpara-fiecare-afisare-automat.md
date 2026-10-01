---
id: DIG-050
title: Publicitatea programatică cumpără fiecare afișare automat, prin licitație în timp real — câștigă eficiență, dar cere date, bugete mari și control asupra plasării
type: zettel
kind: concept
skill: digital-marketing
also: [advertising-strategy, ai-marketing]
level: 2
tags: [programatic, rtb, ad-server, ad-network, ad-exchange, dsp, ssp, dmp, ctv, context-matching]
sources:
  - SRC-029 | cap. 10, p. 272-275
  - SRC-032 | cap. 2.3.4.1, p. 76-77; cap. 5.1, p. 159-171
status: growing
---

# Publicitatea programatică cumpără fiecare afișare automat, prin licitație în timp real — câștigă eficiență, dar cere date, bugete mari și control asupra plasării

> **Ideea în o frază:** în publicitatea programatică (*programmatic advertising*), algoritmii decid în milisecunde, pentru fiecare afișare, dacă o cumpără și cu cât, cât timp se încarcă pagina.

## Explicație

La început, bannerele se inserau manual în codul paginilor și toți vizitatorii vedeau aceeași reclamă. Ambele cărți descriu apoi aceeași evoluție:

- **Ad serverul** stochează, livrează și numără reclamele. Permite *roadblock* (un singur advertiser pe pagină), plafon de frecvență (*frequency capping*) și **secvențiere** (reclame văzute într-o anumită ordine).
- **Rețeaua de publicitate** (*ad network*) cumpără inventar de la publisheri și îl revinde pe categorii. Prețurile sunt stabile, dar transparența e mică, rămâne inventar nevândut și aceeași persoană vede reclama de prea multe ori, pe rețele diferite.
- **Bursa** (*ad exchange*) e o piață deschisă cu **licitație în timp real** (*real-time bidding*, RTB). Advertiserul fixează CPM-ul maxim, publisherul prețul minim, iar sistemul decide instantaneu.
- **DSP** e software-ul advertiserului care licitează pe mai multe burse, **SSP** e software-ul publisherului, iar **DMP** stochează datele de audiență (first-, second- și third-party).

Schwarz-Musch et al. citează că, în 2022, circa 87% din display-ul global era cumpărat programatic (PwC/IAB). Creația poate fi adaptată fiecărui profil prin bannere dinamice, plata se poate lega de orice KPI măsurabil, iar modelul se extinde la TV-ul conectat.

**Unde diferă autorii.** Zahay et al. tratează programaticul ca standard operațional; în cascada lor de obiective apare ținta „display 100% programatic în doi ani”. Schwarz-Musch et al. adaugă critica lui Lammenett. Programaticul e eficient doar cu multe date și bugete de ordinul a cinci-șase cifre. Optimizează spre CTR și impresii, deși contextul în care apare reclama contează (*context matching*). Și aduce o pierdere de control.

## Aplicare

- Înainte să recomanzi programatic, verifică bugetul și volumul de date ale clientului.
- Cere lista de site-uri și setările de brand safety și anti-fraudă, nu doar CPM-ul obținut.
- Definește tu obiectivele și KPI-urile; spre deosebire de Meta sau Google, platformele programatice nu le propun implicit.
- Gândește creația ca serie: secvențierea și plafonul de frecvență sunt și unelte narative.

## Exemplu

Cazul bucătăriilor din SRC-032 parcurge tot lanțul: date imobiliare într-un DMP, un DSP pentru reach și bannere dinamice care schimbă bucătăria și prețul după profil.

## Întrebări

- Dacă algoritmul alege plasarea, cine răspunde pentru contextul în care apare reclama?
- Ce riscuri de siguranță a brandului aduce cumpărarea automată pe mii de site-uri?

## Legături

- **fundament** [[DIG-046-reclama-display-a-evoluat-de-la-bannerul-static-la-rich|DIG-046]] — formatele display sunt materia primă a programaticului.
- **vezi** [[DIG-051-cazul-bucatariilor-date-imobiliare-anonimizate-un-dmp-un|DIG-051]] — cazul bucătăriilor, programatic de la cap la coadă.
- **vezi** [[DIG-054-setarile-de-calitate-decid-daca-impresiile-platite-conteaza|DIG-054]] — automatizarea face obligatorii setările de brand safety, vizibilitate și frecvență.
- **vezi** [[DIG-064-identitatea-fara-cookie-uri-are-trei-trepte-de-reach|DIG-064]] — identitatea de care depinde targetarea programatică după cookie-uri.
- **contrazice** [[ADV-085-eficienta-publicitatii-digitale-ramane-nedovedita-iar|ADV-085]] — Percy și Rosenbaum-Elliott consideră eficiența publicității digitale nedovedită, cu fraudă și vizibilitate îndoielnică.

## Surse

- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 10, p. 272-275
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 2.3.4.1 (p. 76-77) și 5.1 (p. 159-171)

<!-- backlinks:start -->
## Backlinks

- [[AIM-010-precizie-sau-transparenta-ansamblurile-si-retelele|AIM-010]] _vezi_ — Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică
- [[DIG-046-reclama-display-a-evoluat-de-la-bannerul-static-la-rich|DIG-046]] _vezi_ — Reclama display a evoluat de la bannerul static la rich media și video, dar ideea creativă rămâne umană
- [[DIG-051-cazul-bucatariilor-date-imobiliare-anonimizate-un-dmp-un|DIG-051]] _exemplu_ — Cazul bucătăriilor — date imobiliare anonimizate, un DMP, un DSP și bannere dinamice transformă un pliant pentru toată lumea într-o ofertă pentru fiecare gospodărie
- [[DIG-054-setarile-de-calitate-decid-daca-impresiile-platite-conteaza|DIG-054]] _vezi_ — Setările de calitate decid dacă impresiile plătite contează — brand safety, vizibilitate (viewability) și plafonul de frecvență
- [[DIG-055-frauda-publicitara-se-depisteaza-in-timpul-campaniei-prin|DIG-055]] _vezi_ — Frauda publicitară se depistează în timpul campaniei, prin anomalii, nu după, iar plata pe vânzări verificate o face neatractivă
- [[DIG-056-targetarea-contextuala-urmareste-pagina-cea-comportamentala|DIG-056]] _fundament_ — Targetarea contextuală urmărește pagina, cea comportamentală urmărește omul
- [[DIG-064-identitatea-fara-cookie-uri-are-trei-trepte-de-reach|DIG-064]] _vezi_ — Identitatea fără cookie-uri are trei trepte de reach — canalele proprii sau o singură „grădină închisă", camerele curate de date (data clean rooms) și ID-urile universale
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
