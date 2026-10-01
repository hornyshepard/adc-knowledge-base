---
id: DIG-1023
title: Identitatea fără cookie-uri are trei trepte de reach — canalele proprii sau o singură „grădină închisă", camerele curate de date (data clean rooms) și ID-urile universale
type: zettel
kind: framework
skill: digital-marketing
also: [advertising-strategy]
level: 3
tags: [identity-management, data-clean-rooms, universal-id, walled-gardens, pair, uid2]
sources:
  - SRC-032 | cap. 1.3.5.2, p. 31-34
status: seed
---

# Identitatea fără cookie-uri are trei trepte de reach — canalele proprii sau o singură „grădină închisă", camerele curate de date (data clean rooms) și ID-urile universale

> **Ideea în o frază:** cu cât vrei să-ți recunoști clienții pe mai multe rețele, cu atât ai nevoie de infrastructură mai complexă de identitate, iar fiecare treaptă are alt raport între reach și confidențialitate.

## Explicație

Managementul identității (*identity management*) urmărește ca un utilizator să fie recunoscut la orice punct de contact, în timp, legal și tehnic corect (prin login, e-mail, ID în DMP), ca să se poată construi un profil unic. Autorii descriu trei trepte:

| Treaptă | Unde folosești datele | Reach |
|---|---|---|
| 1 | pe propriile canale sau într-o singură rețea (Meta, Google, Amazon) | mic; cu cât restrângi ținta, cu atât te lovești de limite |
| 2 | pe mai multe rețele, prin *data clean rooms* | mediu |
| 3 | pe foarte multe rețele, printr-un ID universal | mare |

**Camerele curate de date** sunt medii cloud în care mai mulți parteneri (advertiseri, publisheri) își analizează împreună datele, după reguli stricte de protecție. ID-uri criptate, de pildă e-mailuri transformate prin *hashing*, leagă seturile fără să dezvăluie date personale, iar rezultatele ies doar agregat (cohorte, rapoarte). Există *media clean rooms*, ale „grădinilor închise" (*walled gardens*): Google Ads Data Hub și PAIR, Amazon Marketing Cloud (care adaugă date de la Whole Foods și Twitch), și *partner clean rooms*, colaborări bilaterale prin Snowflake sau LiveRamp. Disney a construit una care oferă advertiserilor peste 1.000 de segmente first-party.

**ID-ul universal**: datele proprii se sincronizează cu un identificator unic, comun mai multor publisheri, stocat în cookie-uri primare sau ID-uri persistente. Furnizori: Unified ID 2.0, ID5, IdentityLink, SharedID și alții; industria vrea un standard unic. Dacă se impune, publicitatea ar arăta aproape ca în era cookie-urilor terțe; blocantele de cookie-uri o pot totuși opri.

## Aplicare

- Pentru un client mic: canale proprii + o singură rețea mare. Pentru un brand FMCG mare cu un retailer partener: clean room.
- Întreabă furnizorul ce date ies din clean room: doar agregate sau și liste de utilizatori?

## Exemplu

Disney deschide advertiserilor peste 1.000 de segmente din datele proprii fără să le predea datele brute, iar Amazon își combină datele de cumpărare cu cele de la Whole Foods și Twitch în aceeași cameră curată.

## Întrebări

- Dacă ID-ul universal reface practic lumea cookie-urilor, s-a câștigat ceva pentru confidențialitate?

## Legături

- **extinde** [[DIG-1021-strategia-first-party-incepe-cu-intrebarea-de-vanzari|DIG-1021]] — datele first-party sunt materia primă a celor trei trepte.
- **vezi** [[DIG-1017-cookie-urile-terte-ce-faceau-si-de-ce-dispar|DIG-1017]] — de ce a devenit necesară o nouă infrastructură de identitate.
- **vezi** [[DIG-1029-publicitatea-programatica-licitatie-in-timp-real|DIG-1029]] — programmatic-ul folosește aceste identități pentru cumpărarea automată.

## Surse

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 1.3.5.2 (p. 31–34)

<!-- backlinks:start -->
## Backlinks

- [[DIG-1021-strategia-first-party-incepe-cu-intrebarea-de-vanzari|DIG-1021]] _vezi_ — O strategie de date first-party începe cu întrebarea „ce date ne cresc vânzările?", nu cu colectarea, și funcționează doar dacă oferă utilizatorului o valoare reală în schimb
- [[DIG-1029-publicitatea-programatica-licitatie-in-timp-real|DIG-1029]] _vezi_ — Publicitatea programatică cumpără fiecare impresie automat, prin licitație în timp real — câștigă eficiență, pierde control și are nevoie de date și bugete mari
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
