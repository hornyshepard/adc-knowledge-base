---
id: DIG-0922
title: Publicitatea programatică cumpără afișări automat, prin licitație în timp real, în milisecundele în care se încarcă pagina
type: zettel
kind: concept
skill: digital-marketing
also: [advertising-strategy, ai-marketing]
level: 2
tags: [programatic, rtb, ad-server, ad-network, ad-exchange, dsp, ssp, dmp]
sources:
  - SRC-029 | cap. 10, p. 272-275
status: seed
---

# Publicitatea programatică cumpără afișări automat, prin licitație în timp real, în milisecundele în care se încarcă pagina

> **Ideea în o frază:** în publicitatea programatică (*programmatic advertising*), alegerea reclamei, licitația și livrarea se fac automat, cu date și învățare automată, cât timp se încarcă pagina vizitatorului.

## Explicație

La început, reclamele erau „lipite" de mână pe site-uri și toți vizitatorii vedeau aceeași; *Million Dollar Homepage* (2005), o pânză de un milion de pixeli vânduți cu un dolar bucata, e un artefact al acelei epoci. Azi lanțul are mai multe verigi:

- **Ad serverul** stochează reclamele, le livrează și le urmărește. Permite *roadblock* (un singur advertiser pe pagină), exclusivitate față de concurenți, **frequency capping** (limita de afișări pe persoană) și **secvențiere** (reclame văzute într-o ordine anume, ca o poveste în episoade).
- **Rețeaua de publicitate** (*ad network*, de ex. AdSense) e un intermediar: cumpără inventarul de la publisheri și îl revinde pe categorii; prețuri stabile, transparență mică.
- **Bursa de publicitate** (*ad exchange*) e o piață deschisă în care advertiserii și publisherii tranzacționează direct, prin licitație în timp real (**RTB**), ca la bursa de acțiuni; prețul fluctuează, transparența e mai mare.
- **DSP** (*demand-side platform*) — software-ul advertiserului care licitează pe mai multe burse; **SSP** (*supply-side platform*) — software-ul publisherului care își vinde spațiile; **DMP** (*data management platform*) — stochează și analizează datele de audiență ca să țintească segmentele potrivite.

Rețelele au rezolvat agregarea ofertei, dar au lăsat inventar nevândut și au dus la afișări repetate aceleiași persoane pe rețele diferite; programaticul a apărut ca răspuns.

## Aplicare

- Când planifici o campanie programatică, gândește creația ca serie: secvențierea și frequency capping-ul sunt unelte narative, nu doar tehnice.
- Cere transparență: pe ce site-uri a apărut reclama? Contextul afectează brandul.
- Fă inventarul de date înainte: ce segmente vin din DMP și sunt ele conforme cu GDPR?

## Exemplu

Cascada de obiective din cartea despre site-uri include un obiectiv tipic de departament: „publicitatea display 100% programatică în doi ani" (fig. 6.7b) — semn că programaticul e tratat ca standard operațional, nu ca experiment.

## Întrebări

- Ce riscuri de siguranță a brandului (*brand safety*) aduce cumpărarea automată pe mii de site-uri?
- Dacă algoritmul alege plasarea, cine răspunde pentru contextul în care apare reclama?

## Legături

- **fundament** [[DIG-0921]] — formatele display sunt materia primă a programaticului.
- **extinde** [[DIG-0923]] — DMP-ul și datele de audiență fac posibilă targetarea comportamentală.
- **vezi** [[DIG-0924]] — retargetingul folosește aceeași infrastructură de ad serving.

## Surse

- [[SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 10, p. 272-275
