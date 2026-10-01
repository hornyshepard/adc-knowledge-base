---
id: DIG-0934
title: Modelele de atribuire decid ce canal primește meritul conversiei — și schimbă astfel bugetul
type: zettel
kind: framework
skill: digital-marketing
also: [advertising-strategy]
level: 2
tags: [atribuire, last-click, first-touch, linear, multi-touch, utm, roi]
sources:
  - SRC-030 | cap. 4, cap. 5
  - SRC-029 | cap. 9, p. 262-263
  - SRC-029 | cap. 13, p. 381-382
status: seed
---

# Modelele de atribuire decid ce canal primește meritul conversiei — și schimbă astfel bugetul

> **Ideea în o frază:** când clientul atinge brandul de cinci ori înainte să cumpere, modelul de atribuire (*attribution model*) hotărăște cât din merit primește fiecare touchpoint; alegerea modelului e o decizie strategică, nu una tehnică.

## Explicație

Connors (SRC-030) numește atribuirea „una dintre cele mai mari provocări" ale marketingului multicanal: un om vede o reclamă pe Facebook, apoi un banner de retargeting, primește un newsletter și cumpără după o recenzie. Cine a „vândut"?

| Model | Cum împarte meritul | Ce favorizează |
|---|---|---|
| **Last-touch / last-click** | tot meritul ultimei interacțiuni | canalele de final (search de brand, e-mail, retargeting) |
| **First-touch** | tot sau cel mai mult meritul primei interacțiuni | canalele de descoperire (social, display) |
| **Linear** | merit egal tuturor touchpoint-urilor | o imagine echilibrată, dar naivă |
| **Multi-touch** | merit distribuit după contribuția estimată a fiecăruia | e considerat de Connors cel mai cuprinzător |

Consecința practică: dacă datele arată că reclamele sociale aduc interesul inițial, iar e-mailul închide vânzarea, ambele canale trebuie întărite împreună; sub last-click, socialul ar părea inutil.

Zahay et al. (SRC-029) dau infrastructura: **parametrii UTM** adăugați la linkuri (utm_source, utm_medium, utm_campaign obligatorii; utm_term, utm_content opționale) permit urmărirea clicurilor pe postare, reclamă sau influencer în Google Analytics. Capitolul de B2B adaugă că lead-urile din canale diferite au costuri **și** rate de conversie diferite, deci costul pe lead convertit variază enorm de la un canal la altul.

## Aplicare

- Întreabă clientul ce model de atribuire folosește înainte să accepți KPI-urile campaniei; o campanie de notorietate judecată pe last-click va „pierde" întotdeauna.
- Pune UTM-uri pe fiecare link distribuit: fără ele, mare parte din trafic apare ca „direct" sau „none".
- Completează atribuirea cu teste de incrementalitate (zone sau grupuri fără campanie) când e posibil.

## Exemplu

Linkul fictiv din SRC-029 pentru o postare Instagram despre cercetarea lui Lauren Labrecque despre culoare: `utm_source=instagram&utm_medium=paid_social&utm_campaign=color_marketing_labrecque&utm_content=video_ad&utm_term=color_research` — sursa, mediul, campania, varianta de reclamă și termenul, toate identificabile.

## Întrebări

- Atribuirea multi-touch măsoară corelație (cine a fost atins), nu cauzalitate (cine ar fi cumpărat oricum). Ce soluții există?
- Cum se atribuie efectul unei campanii TV sau outdoor într-un model digital?

## Legături

- **fundament** [[DIG-0906-un-metric-e-un-numar-un-kpi-arata-progresul-fata-de-obiectiv|DIG-0906]] — KPI-urile pe canal depind de modelul de atribuire.
- **vezi** [[DIG-0924-retargetingul-trebuie-segmentat-dupa-stadiul-din-journey|DIG-0924]] — retargetingul e câștigătorul clasic al atribuirii last-click.
- **vezi** [[SOC-0905-valid-metrics-framework-succesul-social-se-termina-in-advocacy|SOC-0905]] — impactul social pe vânzări e greu de atribuit, de aceea cadrul se oprește la advocacy.
- **vezi** [[DIG-0931-demand-generation-de-la-continut-la-lead-calificat|DIG-0931]] — în B2B se calculează costul pe lead convertit pe canal.

## Surse

- [[SRC-030-digital-marketing-strategies|SRC-030]] K. Connors, *Advanced Digital Marketing Strategies*, cap. 4, cap. 5
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 9, p. 262-263; cap. 13, p. 381-382

<!-- backlinks:start -->
## Backlinks

- [[DIG-0906-un-metric-e-un-numar-un-kpi-arata-progresul-fata-de-obiectiv|DIG-0906]] _vezi_ — Un metric e doar un număr; un KPI arată cât de aproape ești de obiectiv
- [[DIG-0924-retargetingul-trebuie-segmentat-dupa-stadiul-din-journey|DIG-0924]] _vezi_ — Retargetingul trebuie segmentat după stadiul din journey și dozat, altfel devine hărțuire
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-030-digital-marketing-strategies|SRC-030]] — Advanced Digital Marketing Strategies: Mastering SEO, Social Media, Content Marketing, and AI for Maximum Online Growth
<!-- backlinks:end -->
