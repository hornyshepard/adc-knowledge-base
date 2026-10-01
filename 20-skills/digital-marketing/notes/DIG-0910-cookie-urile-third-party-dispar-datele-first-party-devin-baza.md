---
id: DIG-0910
title: Cookie-urile third-party dispar, iar datele first-party devin baza targetării
type: zettel
kind: concept
skill: digital-marketing
also: [ai-marketing]
level: 2
tags: [cookies, first-party-data, third-party-data, gdpr, ccpa, hashed-email, privacy]
sources:
  - SRC-029 | cap. 5, p. 135-137
  - SRC-029 | cap. 10, p. 278, 282-283
  - SRC-029 | cap. 8, p. 218-219
status: seed
---

# Cookie-urile third-party dispar, iar datele first-party devin baza targetării

> **Ideea în o frază:** cookie-ul first-party aparține site-ului pe care îl vizitezi și îi ușurează experiența; cookie-ul third-party te urmărește de la un site la altul pentru publicitate — iar presiunea legislativă și a browserelor îl elimină, mutând puterea spre datele proprii ale brandului.

## Explicație

Un **tag** (sau pixel, beacon) este un fragment de cod pe pagină care înregistrează comportamentul; un **cookie** este fișierul text din browser care identifică utilizatorul. Împreună alimentează platforma de metrici. Cookie-urile au fost inventate de Netscape (Lou Montulli) ca să nu se golească coșul de cumpărături; inventatorul recunoaște că n-a anticipat interacțiunea cu conținutul încorporat din alte servere, de unde s-au născut cookie-urile third-party.

| | First-party | Third-party |
|---|---|---|
| Cine îl creează | site-ul vizitat | ad serverul / alt domeniu |
| Unde funcționează | doar pe acel site | pe orice site care încarcă acel cod |
| Folosință | logare, coș, analytics (GA4) | retargeting, profiluri cross-site |

Firefox și Safari le-au blocat din 2019; Google a anunțat eliminarea și a amânat-o de mai multe ori. În paralel, **GDPR** (UE, 2018, amenzi de zeci de milioane de euro) și **CCPA** (California: dreptul de a ști, de a șterge, de a refuza vânzarea datelor) au schimbat regulile. Apple iOS 14.5 a permis utilizatorilor să oprească urmărirea între aplicații. Alternativele discutate de autori: un ID universal controlat de utilizator, mai multă **publicitate contextuală**, **e-mailul hash-uit** (un identificator criptografic ireversibil, valabil pe dispozitive diferite) și, mai ales, colectarea de **date first-party** (sondaje, e-mail, chatbot, SMS).

## Aplicare

- Orice strategie digitală nouă trebuie să răspundă: ce date proprii colectăm, cu ce schimb de valoare (reducere, conținut, serviciu)?
- Pentru creativi: ofertele de tip „înscrie-te și primești" devin infrastructură, nu doar promoții.
- Verifică la fiecare campanie conformitatea cu GDPR: consimțământ, transparență, dreptul de retragere.

## Exemplu

Magnolia Bakery (cap. 11) a construit liste proprii prin pop-up cu 10% reducere și o tombolă de ziua de naștere promovată pe social; abonații petreceau cu 35% mai mult timp pe site decât ceilalți.

## Întrebări

- Este targetarea comportamentală incompatibilă cu respectul pentru client sau doar trebuie făcută transparent?
- Ce câștigă și ce pierd brandurile mici, fără baze de date mari, în lumea post-cookie?

## Legături

- **fundament** [[DIG-0901-marketingul-digital-inseamna-interactiune-engagement-masurare|DIG-0901]] — definiția Zahay anticipa deja trecerea la date first-party.
- **extinde** [[DIG-0923-targetarea-contextuala-vs-comportamentala|DIG-0923]] — targetarea comportamentală prin cookie-uri e exact ce se schimbă.
- **aplicare** [[DIG-0926-permisiunea-in-email-are-patru-niveluri|DIG-0926]] — permisiunea în e-mail este cea mai solidă sursă de date first-party.
- **vezi** [[DIG-0924-retargetingul-trebuie-segmentat-dupa-stadiul-din-journey|DIG-0924]] — retargetingul depinde de pixeli și cookie-uri.

## Surse

- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 5, p. 135-137; cap. 8, p. 218-219; cap. 10, p. 278, 282-283

<!-- backlinks:start -->
## Backlinks

- [[DIG-0901-marketingul-digital-inseamna-interactiune-engagement-masurare|DIG-0901]] _vezi_ — Marketingul digital înseamnă interacțiune, engagement și măsurare, nu doar canale noi
- [[DIG-0923-targetarea-contextuala-vs-comportamentala|DIG-0923]] _vezi_ — Targetarea contextuală urmărește pagina, cea comportamentală urmărește omul
- [[DIG-0926-permisiunea-in-email-are-patru-niveluri|DIG-0926]] _vezi_ — Permisiunea în e-mail marketing are patru niveluri, de la opt-out la double opt-in
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
<!-- backlinks:end -->
