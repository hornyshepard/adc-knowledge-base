---
id: DIG-036
title: În e-mailul cu AI, momentul și frecvența trimiterii se optimizează pe individ, nu pe listă
type: zettel
kind: method
skill: digital-marketing
also: [ai-marketing]
level: 2
tags: [email-marketing, send-time-optimization, automatizare, customer-journey]
sources:
  - SRC-037 | cap. 7 (7.2-7.6)
  - SRC-040 | secț. 4, cap. 2 (Contact Strategy)
status: growing
---

# În e-mailul cu AI, momentul și frecvența trimiterii se optimizează pe individ, nu pe listă

> **Ideea în o frază:** pe lângă conținutul personalizat, AI schimbă două variabile pe care e-mailul clasic le fixa pentru toată lista: ora trimiterii și ritmul.

## Explicație

Capitolul despre e-mail din cartea lui Noil descrie cinci pârghii AI:

| Pârghie | Ce face |
|---|---|
| Segmentare cu AI | grupuri fine, dinamice (ex.: au văzut produse scumpe, n-au cumpărat) |
| Personalizare predictivă | estimează ce produs va interesa și când va cumpăra omul |
| Conținut dinamic | subiect, recomandări și blocuri de text se schimbă după profil |
| Optimizarea momentului (*send time optimization*) | fiecare primește mesajul la ora la care obișnuiește să deschidă |
| Optimizarea frecvenței | ritmul se reglează după implicare, ca să eviți oboseala și dezabonarea |

Cartea le aplică pe patru e-mailuri de ciclu de viață: **bun venit** (recomandări după ce a răsfoit omul înainte de abonare), **coș abandonat** (produsul lăsat + produse înrudite, eventual stoc limitat), **post-cumpărare** (produse complementare, tutoriale) și **reactivare** (ofertă pentru cei inactivi de luni de zile).

Două avertismente: supra-personalizarea (mesajul pare că „știe prea mult") și pierderea vocii brandului în automatizare. Noil recomandă ca un om să verifice conținutul generat.

Richards și McLean ([[SRC-040-intelligent-customer-engagement|SRC-040]]) adaugă stratul de reguli de deasupra algoritmului: o **strategie de contact** scrisă (frecvență maximă pe canal și pe produs, ferestre orare), care nu poate fi încălcată de managerii de produs dornici să-și trimită campaniile.

## Aplicare

- Scrie fluxurile de e-mail ca **scenarii** (declanșator → mesaj → regulă de continuare), nu ca newslettere izolate.
- Testează A/B subiecte și CTA-uri, dar lasă ora și frecvența în seama algoritmului abia după ce ai suficiente date.
- Copywriterul definește tonul și limitele vocii brandului; instrumentele de tip Phrasee (subiecte generate prin NLG) lucrează în interiorul lor.

## Exemplu

Un serviciu de abonament fitness, în exemplul din carte, trimite planul săptămânal de antrenament fiecărui abonat la ora la care acesta deschide de obicei e-mailurile, nu la aceeași oră pentru toți.

## Întrebări

- Ce se întâmplă cu „momentul campaniei" (lansarea simultană) dacă fiecare primește mesajul la altă oră?
- Când o frecvență redusă e mai profitabilă decât una mare, chiar dacă scade numărul de clicuri?

## Legături

- **extinde** [[DIG-034-e-mailul-promotional-bun-are-o-singura-oferta-un-termen|DIG-034]] — regulile e-mailului promoțional, cu ora și frecvența lăsate algoritmului.
- **aplicare** [[AIM-017-segmentele-construite-cu-ai-sunt-dinamice-clientul-migreaza|AIM-017]] — fluxurile de e-mail activează segmentele dinamice.
- **aplicare** [[AIM-016-personalizarea-cu-ai-lucreaza-in-patru-registre-in-timp|AIM-016]] — e-mailul combină registrele comportamental și predictiv.
- **vezi** [[DIG-069-personalizarea-functioneaza-doar-cu-relevanta-respect-si|DIG-069]] — supra-personalizarea, riscul numit și de Noil.
- **vezi** [[AIM-019-ofera-ce-e-mai-probabil-sa-accepte-clientul-nu-ce-aduce|AIM-019]] — strategia de contact și arbitrajul ofertelor în sistemele automate.

## Surse

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, cap. 7 (7.2-7.6)
- [[SRC-040-intelligent-customer-engagement|SRC-040]] Aly Richards & Scott McLean, *Intelligent Customer Engagement*, secț. 4, cap. 2

<!-- backlinks:start -->
## Backlinks

- [[AIM-003-martech-are-sapte-cazuri-de-utilizare-pe-calea-clientului|AIM-003]] _vezi_ — Martech are șapte cazuri de utilizare pe calea clientului — de la publicitate și conținut la service CRM
- [[AIM-017-segmentele-construite-cu-ai-sunt-dinamice-clientul-migreaza|AIM-017]] _vezi_ — Segmentele construite cu AI sunt dinamice — clientul migrează între ele după comportament
- [[AIM-019-ofera-ce-e-mai-probabil-sa-accepte-clientul-nu-ce-aduce|AIM-019]] _vezi_ — Oferă ce e mai probabil să accepte clientul, nu ce aduce marja cea mai mare — un „da" aduce alt „da"
- [[CPY-029-vocea-brandului-nu-se-obtine-din-prompt-ci-dintr-un-ciclu|CPY-029]] _vezi_ — Vocea brandului nu se obține din prompt, ci dintr-un ciclu exemple → ciornă → editare umană → feedback → control final
- [[DIG-034-e-mailul-promotional-bun-are-o-singura-oferta-un-termen|DIG-034]] _vezi_ — E-mailul promoțional bun are o singură ofertă, un termen-limită și un subiect sub 50 de caractere
- [[DIG-035-in-e-mail-click-to-open-rate-spune-mai-mult-decat-open-rate|DIG-035]] _vezi_ — În e-mail, click-to-open rate spune mai mult decât open rate
- [[SRC-037-ai-driven-marketing|SRC-037]] — AI-Driven Marketing: Harnessing Artificial Intelligence to Personalize Customer Experiences
- [[SRC-040-intelligent-customer-engagement|SRC-040]] — Intelligent Customer Engagement: The Future of Content Marketing
<!-- backlinks:end -->
