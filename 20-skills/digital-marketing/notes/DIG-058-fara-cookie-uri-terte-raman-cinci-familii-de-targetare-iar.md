---
id: DIG-058
title: Fără cookie-uri terțe rămân cinci familii de targetare, iar profilul pe cookie descria oricum un dispozitiv, nu un om
type: zettel
kind: framework
skill: digital-marketing
also: [advertising-strategy, ai-marketing]
level: 2
tags: [targetare, post-cookie, contextual, semantic, predictiv, cohorte, topics-api, first-party]
sources:
  - SRC-032 | cap. 1.2.3-1.3.4, p. 19-26
status: growing
---

# Fără cookie-uri terțe rămân cinci familii de targetare, iar profilul pe cookie descria oricum un dispozitiv, nu un om

> **Ideea în o frază:** pierderea cookie-urilor nu e atât de mare pe cât pare, pentru că profilurile erau imprecise, iar targetarea fără ele există de la începuturile publicității.

## Explicație

**Limita ascunsă a cookie-urilor.** Profilul construit din navigare aparține unui dispozitiv (telefon, tabletă, smart TV), pe care îl pot folosi mai mulți oameni. Fără autentificare, comportamentul unei persoane nu poate fi urmărit de pe un dispozitiv pe altul. Deci un profil exact al unui individ nu a existat niciodată. Autorii susțin că unele campanii bazate pe targetare fără profiluri pot fi chiar mai eficiente.

**Cele cinci opțiuni**, folosite separat sau combinat:

| Opțiune | Principiu | Limită |
|---|---|---|
| Contextuală | reclama apare într-un mediu tematic potrivit | omonime, contexte sensibile, inventar limitat |
| Semantică | AI înțelege tot contextul (text, imagine, video, sentiment), în timp real | cere tehnologie și date de calitate |
| Predictivă | învățare automată pe date colectate prezice acțiuni viitoare | precizia depinde de date și algoritm |
| Cohortă / interes | grupuri de utilizatori cu trăsături comune, nu indivizi | controversă de confidențialitate, nevoie de bază uriașă de date |
| First-party | date date voluntar de clienți | reach limitat, cere schimb de valoare |

Despre cohorte: Google a renunțat în 2022 la FLoC (ID-uri numerice) și a trecut la Topics API. Interesele se calculează local, în browser, se grupează pe teme și se șterg periodic, fără să fie trimise la Google. Criticile rămân: cohortele foarte înguste pot identifica persoane, iar cu peste 60% din piața browserelor Google își poate întări puterea în publicitate.

Fiecare opțiune acoperă de regulă un singur obiectiv; de aceea autorii propun un proces de campanie care le combină cu persone și cu journey-ul.

## Aplicare

- Pentru fiecare obiectiv al campaniei, alege combinația: context pentru awareness, first-party și predictiv pentru conversie.
- Nu cumpăra „audiențe" fără să întrebi pe ce se bazează: context, cohortă, date proprii sau date cumpărate?

## Exemplu

Un e-shop de biciclete electrice poate folosi contextul (site-uri de ciclism), date first-party (cumpărătorii existenți) și predicția (cine citește des blogul e probabil interesat de rucsacuri de tură), fără niciun cookie terț.

## Întrebări

- Dacă profilurile erau atât de imprecise, de ce a fost industria atât de dependentă de ele?

## Legături

- **fundament** [[DIG-057-cookie-urile-terte-au-facut-posibile-retargetingul|DIG-057]] — de ce dispar cookie-urile terțe.
- **vezi** [[DIG-056-targetarea-contextuala-urmareste-pagina-cea-comportamentala|DIG-056]] — distincția de bază: targetarea după pagină sau după om.
- **vezi** [[DIG-059-targetarea-contextuala-pune-reclama-langa-subiectul-deja|DIG-059]] — targetarea contextuală și semantică în detaliu.
- **vezi** [[DIG-060-targetarea-predictiva-muta-intrebarea-de-la-cine-a-fost|DIG-060]] — targetarea predictivă și declanșatorii de context.
- **vezi** [[DIG-062-strategia-de-date-first-party-porneste-de-la-intrebarea-ce|DIG-062]] — strategia de date first-party.

## Surse

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 1.2.3–1.3.4 (p. 19–26)

<!-- backlinks:start -->
## Backlinks

- [[DIG-056-targetarea-contextuala-urmareste-pagina-cea-comportamentala|DIG-056]] _vezi_ — Targetarea contextuală urmărește pagina, cea comportamentală urmărește omul
- [[DIG-057-cookie-urile-terte-au-facut-posibile-retargetingul|DIG-057]] _vezi_ — Cookie-urile terțe au făcut posibile retargetingul, lookalike-urile și profilurile cross-site, iar legea și browserele le scot din joc — puterea trece la datele first-party
- [[DIG-059-targetarea-contextuala-pune-reclama-langa-subiectul-deja|DIG-059]] _extinde_ — Targetarea contextuală pune reclama lângă subiectul deja prezent în mintea cititorului, iar versiunea semantică citește și sentimentul contextului
- [[DIG-060-targetarea-predictiva-muta-intrebarea-de-la-cine-a-fost|DIG-060]] _extinde_ — Targetarea predictivă mută întrebarea de la „cine a fost omul" la „ce va face probabil" și poate folosi declanșatori de context precum vremea, locul și ora
- [[DIG-062-strategia-de-date-first-party-porneste-de-la-intrebarea-ce|DIG-062]] _extinde_ — Strategia de date first-party pornește de la întrebarea „ce date ne cresc vânzările?” și obține datele prin invitație și schimb de valoare, nu prin colectare ascunsă
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
