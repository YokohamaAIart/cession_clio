# SESSION SNAPSHOT — Contrat Factory (Clio)
Date: 2026-07-03 · Session: claude.ai chat · Status: DELIVERED, pending proof-read validation

---

## 1. PROJECT STATE

**Built:** One-page French vehicle-sale contract system. 15 themed templates (A–O), one shared content skeleton (same fields everywhere), WeasyPrint HTML→PDF pipeline. 1 real contract filled.

**Template catalogue (all 1-page A4, PDF + editable HTML master in outputs):**

| ID | Theme | ID | Theme |
|---|---|---|---|
| A | Ardoise & Or (sobre, pro) | I | Japon/Yokohama (hanko 契約) |
| B | Sauge & Graphite (cartes) | J | Plan de Vol (boarding pass) |
| C | Startup covoiturage | K | Menu Gastronomique |
| D | Psychédélique | L | Gazette 1900 (« VENDU ! ») |
| E | Aérospatial (mission-control) | M | Día de los Muertos (calavera WM) |
| F | USA 250 (flag tramé 30% SVG) | N | Atelier garage (graisse/acier) |
| G | Geek LLM (YAML editor) | O | Blueprint (cartouche DWG) |
| H | Art Déco (noir & or) | — | — |

N & O carry an **original crown+hatchback SVG watermark** (MGP-inspired, not copied), tramé 30%.

**Filled contract (the real deliverable):**
`Contrat_Vente_Clio_MEHIDI_REMPLI.pdf` — template A, Dos Santos → Mehidi.

## 2. REAL CONTRACT — DATA REGISTER

**Direction (LOCKED by user):** DOS SANTOS vend à MEHIDI. Point barre.
Mechanism: négociant achat-revente flash même jour (modèle Autohero/Auto1) — récépissé R.322-4 (pro acquéreur) + cession Cerfa 15776*01 le 02/03/2026.

**Confirmed (source = docs officiels uploadés: carte grise, récépissé, Cerfa):**
- Vendeur: DOS SANTOS ALVARELHOS Kevin, 24 Av. Jean-Jacques Rousseau, 93190 Livry-Gargan, SIREN 878 954 130, RCS Bobigny, tél +33 7 53 43 30 56
- Acheteur: MÉHIDI Hakim, né 22/07/1995 à Châlons-en-Champagne, **13 rue de Savigny, Escalier 2, 91390 Morsang-sur-Orge** (adresse carte grise — LOCKED, prime sur le .md Athis-Mons), tél +33 3 65 20 59 422, Hakim.mehidi@yahoo.fr
- Véhicule: Renault Clio V E-Tech Hybride, finition Limited, VIN VF1RJA00168812703, type RJABH2MU4UA3FA5200, immat GF-405-GG, 1re MEC 18/03/2022, 28 500 km, CT jusqu'au 01/10/2027, 67 kW / 5 CV, hybride essence (EH), Euro 6d
- Transaction: 15 800 € (source .md uniquement — à corroborer), virement, 02/03/2026, remise à Athis-Mons (91)

**[À COMPLÉTER] (absent des docs — jamais inventé):**
N° de contrat · IBAN/BIC Dos Santos · nombre de clés · propriétaires précédents

**[à confirmer]:** Régime TVA sur la marge (art. 297 A CGI) — hypothèse négociant, non vérifiée.

## 3. TECHNICAL NOTES (WeasyPrint 69, pipeline)

- Fragments partagés dans `gen_fun.py` (VENDEUR, ACHETEUR, VEHICULE, ITEMS, PAIEMENT, LIVRAISON, SIGNATURES, FOOTER, BASE, FILLS). gen_fun2–5 les importent.
- **Gotchas résolus:** (1) pas de shorthand gradient 2-positions `color 0 24px` → stops explicites obligatoires; (2) `background-clip:text` non supporté; (3) watermark = div `position:fixed; z-index:-1` + SVG en data-URI, surfaces au-dessus en `rgba(255,255,255,.7)` pour ghosting; (4) éléments fixed sans z-index négatif peignent PAR-DESSUS le contenu.
- Fonts dispo: Poppins, Lora, Liberation, DejaVu (+ Mono), IPA/Noto CJK.
- Rendu: `HTML(string=..., base_url='.').write_pdf(...)`; contrôle 1 page via `pdfinfo | grep Pages`; vérif par `pdftotext` + pixel-sampling PIL (l'outil view d'images a glitché en fin de session — validation non-visuelle fiable).

## 4. OPEN ITEMS

1. **Proof-read du contrat MEHIDI** — livré, en attente retour utilisateur (dernière demande: "draft latest contrat for proof reading" → livré tel quel, aucune modif depuis la correction propriétaires/adresse).
2. Compléter: N° contrat, IBAN/BIC, clés, propriétaires précédents.
3. Trancher TVA marge vs TVA totale avant signature.
4. Prix 15 800 € — corroborer (une seule source).
5. Optionnel: décliner le contrat rempli sur N (Atelier) ou O (Blueprint) si le look A ne convient pas.

## 5. FILES (persistent — /outputs de cette session)

- `Contrat_Vente_Clio_MEHIDI_REMPLI.pdf` + `_source.html` ← LE livrable
- `Contrat_Vente_Clio_[A–O]_*.pdf` + `_source.html` ← 15 templates vierges
- `contrat_factory_sources.zip` ← **tous les scripts générateurs + masters HTML** (22 fichiers). Le conteneur reset entre sessions: ce zip est la seule sauvegarde du pipeline.

---

# NEXT SESSION — RESTART PROMPT (paste-ready)

```
CONTEXT RESTORE — Contrat Factory Clio.

Upload: contrat_factory_sources.zip (pipeline complet) et/ou Contrat_Vente_Clio_MEHIDI_source.html.

State: 15 templates one-page (A–O) opérationnels, pipeline WeasyPrint
(gotchas connus: gradients à stops explicites, watermark = fixed div
z-index:-1 + SVG data-URI, pas de background-clip:text).

Contrat réel livré: Dos Santos (négociant, SIREN 878 954 130, Livry-Gargan)
VEND à Méhidi Hakim (13 rue de Savigny, Esc. 2, 91390 Morsang-sur-Orge —
adresse carte grise, LOCKED). Clio V E-Tech Hybride Limited,
VIN VF1RJA00168812703, GF-405-GG, 1re MEC 18/03/2022, 28 500 km,
CT 01/10/2027, 15 800 € virement, 02/03/2026, remise Athis-Mons.
Sens de la vente verrouillé par l'utilisateur — ne pas re-questionner.

Restent [À COMPLÉTER]: N° contrat, IBAN/BIC vendeur, nb clés,
propriétaires précédents. [À confirmer]: TVA marge art. 297 A CGI.
Prix 15 800 € = source unique (.md), non corroboré.

Task now: <insérer la tâche — ex. corrections proof-read / compléter
champs / décliner sur template N ou O>.

Rules: données docs officiels = autoritaires; jamais inventer un champ
manquant → [À COMPLÉTER]; redraft = fichier complet; une page A4.
```

*Unzip → `pip install weasyprint --break-system-packages` → `python3 gen_fun.py` régénère A–F, gen_fun2–5 le reste, `fill_real.py` refait le contrat Mehidi.*
