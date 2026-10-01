---
id: DIG-1035
title: Retargetingul a fost cea mai eficientă tactică a erei cookie și este cea mai expusă după ea — funcționează doar cu urmărire consimțită, pixeli necesari și plafoane de frecvență
type: zettel
kind: concept
skill: digital-marketing
also: [social-influencer]
level: 2
tags: [retargeting, remarketing, meta-pixel, tracking-pixel, dynamic-remarketing, post-cookie]
sources:
  - SRC-032 | cap. 1.2.1, p. 15-16; cap. 1.2.3, p. 19; cap. 3.2, p. 102
  - SRC-031 | cap. 3, p. 90; cap. 6, p. 200; cap. 11, p. 391-392
  - SRC-033 | secț. 15 „Creating A Facebook Remarketing Campaign"
status: seed
---

# Retargetingul a fost cea mai eficientă tactică a erei cookie și este cea mai expusă după ea — funcționează doar cu urmărire consimțită, pixeli necesari și plafoane de frecvență

> **Ideea în o frază:** a arăta din nou reclama celor care au fost deja interesați e eficient, dar depinde exact de urmărirea pe care legea și browserele o limitează.

## Explicație

**Mecanismul.** Pe site se instalează un cod de urmărire: cookie, cod Google Analytics sau pixel (de exemplu, Meta Pixel, care leagă acțiunile vizitatorilor de conturile lor de Facebook). Cine a vizitat anumite pagini primește apoi reclame în alte locuri: YouTube, Gmail, feed-ul de Facebook. Remarketingul dinamic arată chiar produsul văzut, cu imagine și preț (Sachdev). Unii oameni au nevoie doar de o amintire, alții de un stimulent.

**De ce e expus.** Fără cookie-uri terțe, retargetingul cuprinzător pe mai multe rețele de reclame nu mai e posibil (SRC-032). Google a redenumit retargetingul în rapoarte („your data"), elimină treptat audiențele similare și interzice informațiile „sensibile" în listele de remarketing. Recomandările lui Sachdev pentru pixeli: consimțământ, doar pixelii necesari pentru ținta ta, posibilitatea de a refuza urmărirea.

**Varianta „rețetă".** Nishad (SRC-033) arată pașii pe Facebook: instalezi pixelul în antetul site-ului, adaugi evenimentul „ViewContent", creezi o campanie cu obiectiv de conversie și refolosești o postare existentă ca reclamă. Ghidul nu spune nimic despre consimțământ, ceea ce arată cât de repede s-a schimbat contextul.

## Aplicare

- Exclude din retargeting cumpărătorii recenți și pune un plafon de frecvență.
- Construiește listele pe date first-party consimțite (abonați, clienți autentificați), nu doar pe pixeli.
- Gândește creativ secvența: a doua reclamă nu trebuie să repete prima, ci să răspundă motivului probabil pentru care omul a plecat.

## Exemplu

Exemplul din SRC-032 arată și eșecul: după ce citești despre Roma, ești urmărit de reclame la zboruri și hoteluri, apoi de un voucher. Un sistem prost setat îți arată reclama companiei aeriene și la câteva săptămâni după ce ai cumpărat deja biletul.

## Întrebări

- Când devine retargetingul hărțuire? Ce frecvență ai accepta tu?
- Dacă retargetingul apare excelent în rapoartele last-click, cât din succes e meritul lui și cât al reclamelor de dinainte?

## Legături

- **fundament** [[DIG-1017-cookie-urile-terte-ce-faceau-si-de-ce-dispar|DIG-1017]] — tehnologia de care depindea retargetingul clasic.
- **vezi** [[DIG-1022-consimtamantul-valid-activ-retras-la-fel-de-usor|DIG-1022]] — urmărirea are nevoie de consimțământ valid.
- **vezi** [[DIG-1027-brand-safety-viewability-si-plafonul-de-frecventa|DIG-1027]] — plafonul de frecvență protejează de suprasaturare.
- **vezi** [[SOC-1004-scara-facebook-de-la-organic-la-remarketing|SOC-1004]] — remarketingul e ultima treaptă a scării de pe Facebook.

## Surse

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 1.2.1 (p. 15–16), 1.2.3 (p. 19), 3.2 (p. 102)
- [[SRC-031-digital-marketing-manual|SRC-031]] Raj Sachdev, *Digital Marketing*, cap. 3 (p. 90), cap. 6 (p. 200), cap. 11 (p. 391–392)
- [[SRC-033-facebook-marketing|SRC-033]] Bharat Bhuval Nishad, *Facebook Marketing & Facebook Ads Beginner To Pro*, secț. „Creating A Facebook Remarketing Campaign"

<!-- backlinks:start -->
## Backlinks

- [[DIG-1005-palnia-de-conversie-digitala-aida-este-parcursa-neliniar|DIG-1005]] _vezi_ — Pâlnia de conversie digitală (AIDA digital) descrie etapele, dar cumpărătorul real le parcurge neliniar, cu întreruperi și pe mai multe dispozitive
- [[DIG-1017-cookie-urile-terte-ce-faceau-si-de-ce-dispar|DIG-1017]] _vezi_ — Cookie-urile terțe au făcut posibile retargetingul, lookalike-urile și optimizarea în timp real, iar reglementarea și browserele le scot treptat din joc
- [[DIG-1030-cazul-bucatariilor-dmp-dsp-si-bannere-dinamice|DIG-1030]] _vezi_ — Cazul bucătăriilor — date imobiliare anonimizate, un DMP, un DSP și bannere dinamice transformă un pliant pentru toată lumea într-o ofertă pentru fiecare gospodărie
- [[DIG-1033-atribuirea-devine-incerta-etapele-de-inceput-dezavantajate|DIG-1033]] _vezi_ — Atribuirea vânzării pe touchpoint-uri devine tot mai incertă după cookie-uri — modelele first-touch și last-touch simplifică, iar etapele de început ies dezavantajate
- [[SOC-1004-scara-facebook-de-la-organic-la-remarketing|SOC-1004]] _vezi_ — Pe Facebook, marketingul urcă o scară — prezență organică, engagement, lead-uri, trafic plătit, remarketing —, pentru că reach-ul organic singur nu mai ajunge
- [[SRC-031-digital-marketing-manual|SRC-031]] — Digital Marketing
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
- [[SRC-033-facebook-marketing|SRC-033]] — Facebook Marketing & Facebook Ads Beginner To Pro
<!-- backlinks:end -->
