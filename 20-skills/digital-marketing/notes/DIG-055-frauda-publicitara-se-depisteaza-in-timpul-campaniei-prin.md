---
id: DIG-055
title: Frauda publicitară se depistează în timpul campaniei, prin anomalii, nu după, iar plata pe vânzări verificate o face neatractivă
type: zettel
kind: checklist
skill: digital-marketing
also: [client-business]
level: 2
tags: [ad-fraud, boti, domain-spoofing, programmatic, verificare, anomalii]
sources:
  - SRC-032 | cap. 2.3.4.2, p. 78; cap. 5.1.1.2, p. 162; cap. 5.2.3, p. 175-177
status: growing
---

# Frauda publicitară se depistează în timpul campaniei, prin anomalii, nu după, iar plata pe vânzări verificate o face neatractivă

> **Ideea în o frază:** în programmatic, o parte din impresii și clicuri pot fi fabricate de roboți; advertiserul se apără prin verificarea furnizorilor, urmărirea anomaliilor în timp real și modele de plată greu de falsificat.

## Explicație

**Tipuri de fraudă** (după Sadeghpour și Vlajic): *placement fraud* (reclame pe site-uri frauduloase sau în zone invizibile ale unor site-uri legitime), *traffic fraud* (boți și „ferme de clicuri" care umflă impresiile și clicurile), *action fraud* (formulare și cumpărări false, generate ca să încaseze comisioane). Campaniile programmatic au o rată de fraudă mai mare decât cele digitale clasice. *Domain spoofing*: traficul e trimis pe un domeniu care imită unul legitim, uneori pe copii ale unor site-uri de încredere.

**Măsuri recomandate:**

- ceri platformelor și furnizorilor de RTB precauțiile anti-fraudă și certificatele;
- liste albe de publisheri și verificarea plasării (*ad verification*);
- KPI de performanță cu plată doar pe cumpărări verificate în magazinul propriu, pentru că acestea nu îi interesează pe fraudatori (dar se potrivește doar campaniilor de vânzare);
- urmărești anomaliile: CTR neobișnuit de mare, trafic din țări îndepărtate la ore suspecte, afișări care durează în medie o secundă, „vizualizări" fără interacțiune umană; un bot poate falsifica și vizibilitatea derulând pagina;
- verifici aleatoriu touchpoint-urile: cele legitime au date de identificare a editorului și apar pe liste de încredere;
- folosești detecție automată în timpul campaniei, nu analize după.

## Aplicare

- Stabilește praguri de alarmă (CTR, geografie, ore) înainte de lansare și verifică săptămânal.
- Când un raport arată rezultate „prea bune", tratează-l ca pe un semnal de verificat, nu ca pe un succes.

## Exemplu

Cu un ad server propriu, anomalia sare în ochi: 1.000 de clicuri la ora 4 dimineața pe 10.000 de afișări, când într-o noapte obișnuită la ora aceea se difuzează 50 de afișări cu 2 clicuri.

## Întrebări

- Cine plătește impresiile frauduloase descoperite după campanie: advertiserul, agenția sau platforma?

## Legături

- **vezi** [[DIG-054-setarile-de-calitate-decid-daca-impresiile-platite-conteaza|DIG-054]] — celelalte setări de calitate ale campaniei.
- **vezi** [[DIG-042-modelul-de-plata-media-se-alege-dupa-obiectiv-si-etapa-din|DIG-042]] — modelul de plată CPA ca protecție.
- **vezi** [[DIG-050-publicitatea-programatica-cumpara-fiecare-afisare-automat|DIG-050]] — de ce programaticul e mai expus.
- **vezi** [[SOC-029-audienta-unui-influencer-se-verifica-inainte-de-orice|SOC-029]] — semnalele de fraudă se verifică și înainte de contractul cu un influencer.
- **vezi** [[ADV-085-eficienta-publicitatii-digitale-ramane-nedovedita-iar|ADV-085]] — frauda e unul dintre motivele pentru care eficiența digitală rămâne contestată.

## Surse

- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 2.3.4.2 (p. 78), 5.1.1.2 (p. 162), 5.2.3 (p. 175–177)

<!-- backlinks:start -->
## Backlinks

- [[ADV-085-eficienta-publicitatii-digitale-ramane-nedovedita-iar|ADV-085]] _vezi_ — Eficiența publicității digitale rămâne nedovedită, iar cartea vede rețelele sociale ca un mediu „negociat", afectat de fraudă și de vizibilitate slabă
- [[DIG-042-modelul-de-plata-media-se-alege-dupa-obiectiv-si-etapa-din|DIG-042]] _vezi_ — Modelul de plată media se alege după obiectiv și etapa din customer journey — CPM pentru notorietate, CPV/CPE pentru atracție, CPC/CPL pentru informare, CPA pentru cumpărare
- [[DIG-054-setarile-de-calitate-decid-daca-impresiile-platite-conteaza|DIG-054]] _vezi_ — Setările de calitate decid dacă impresiile plătite contează — brand safety, vizibilitate (viewability) și plafonul de frecvență
- [[SOC-029-audienta-unui-influencer-se-verifica-inainte-de-orice|SOC-029]] _vezi_ — Audiența unui influencer se verifică înainte de orice contract — semnale de fraudă, autenticitatea angajamentului și potrivirea publicului, manual sau cu AI
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
