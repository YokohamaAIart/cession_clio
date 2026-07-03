#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 4 themed one-page French vehicle sale contract templates."""
from weasyprint import HTML

# ---------------------------------------------------------------- fragments
VENDEUR = """
    <p>Raison sociale : <span class="fill f-l"></span></p>
    <p>Adresse : <span class="fill f-xl"></span></p>
    <p>SIREN : <span class="fill f-s"></span> — SIRET : <span class="fill f-m"></span></p>
    <p>Tél. : <span class="fill f-s"></span> — Email : <span class="fill f-m"></span></p>
"""

ACHETEUR = """
    <p>Nom, prénom : <span class="fill f-l"></span></p>
    <p>Adresse : <span class="fill f-xl"></span></p>
    <p>Tél. : <span class="fill f-s"></span> — Email : <span class="fill f-m"></span></p>
    <p>Pièce d'identité (type et n°) : <span class="fill f-m"></span></p>
"""

VEHICULE = """
    <tr><td class="k">Marque, modèle | Puissance</td><td class="v"><b>Renault Clio 1.0 SCe — 72 ch / 53 kW</b></td></tr>
    <tr><td class="k">VIN | Pays d'origine | N° d'immatriculation</td><td class="v">VF1<span class="fill f-s"></span> | FR | <span class="fill f-s"></span></td></tr>
    <tr><td class="k">Carburant | Moteur d'origine | Classe environnementale</td><td class="v">Essence | Oui | Euro 6</td></tr>
    <tr><td class="k">Kilométrage (non garanti)</td><td class="v"><span class="fill f-s"></span> km</td></tr>
    <tr><td class="k">1<sup>re</sup> mise en circulation | Dernier entretien | CT valable jusqu'au</td><td class="v"><span class="fill f-xs"></span> | <span class="fill f-xs"></span> | <span class="fill f-xs"></span></td></tr>
    <tr><td class="k">Nombre de clés | Propriétaires précédents</td><td class="v"><span class="fill f-xs"></span> | <span class="fill f-xs"></span></td></tr>
    <tr><td class="k">Accidenté | Véhicule de société</td><td class="v"><span class="fill f-xs"></span> | <span class="fill f-xs"></span></td></tr>
    <tr><td class="k">Régime de TVA</td><td class="v"><span class="fill f-m"></span></td></tr>
"""

ITEMS = """
  <tr><td class="pos">01</td><td><b>Voiture — Renault Clio 1.0 SCe</b></td><td class="qty">01</td><td class="num"><span class="fill f-s"></span> €</td></tr>
  <tr class="discount"><td></td><td>Remise commerciale</td><td class="qty"></td><td class="num">− <span class="fill f-xs"></span> €</td></tr>
  <tr><td class="pos">02</td><td>Garantie <span class="fill f-xs"></span> mois</td><td class="qty">01</td><td class="num"><span class="fill f-xs"></span> €</td></tr>
  <tr><td class="pos">03</td><td>Immatriculation (carte grise) par nos soins</td><td class="qty">01</td><td class="num"><span class="fill f-xs"></span> €</td></tr>
  <tr><td class="pos">04</td><td>Préparation &amp; mise à disposition</td><td class="qty">01</td><td class="num"><span class="fill f-xs"></span> €</td></tr>
  <tr><td class="pos">05</td><td>Frais de livraison</td><td class="qty">01</td><td class="num"><span class="fill f-xs"></span> €</td></tr>
"""

PAIEMENT = """
  <div class="pay-meta">
    <div><b>Mode de paiement :</b> Virement bancaire</div>
    <div><b>Montant :</b> <span class="fill f-s"></span> €</div>
  </div>
  <p>Le total doit être réglé par virement bancaire sur le compte suivant avant la livraison :</p>
  <p>Titulaire du compte : <span class="fill f-l"></span></p>
  <p>IBAN : <span class="fill f-xl"></span> &nbsp;&nbsp; BIC : <span class="fill f-s"></span></p>
  <p>Référence à mentionner : <span class="fill f-m"></span></p>
"""

LIVRAISON = """Point de livraison : <span class="fill f-xl"></span> &nbsp;&nbsp; Date prévue : <span class="fill f-s"></span>"""

SIGNATURES = """
<p class="sig-intro">Fait à <span class="fill f-m"></span>, le <span class="fill f-s"></span>, en deux exemplaires originaux, dont un remis à chaque partie.</p>
<div class="sigs">
  <div class="sig"><h4>Le vendeur</h4><p>Signature précédée de la mention « Lu et approuvé »</p></div>
  <div class="sig"><h4>L'acheteur</h4><p>Signature précédée de la mention « Lu et approuvé »</p></div>
</div>
"""

FOOTER = """Raison sociale — Forme juridique — Adresse du siège social — SIREN — SIRET — Capital social (le cas échéant)<br>
Tél. — Email — N° TVA intracommunautaire ou mention du régime applicable (à compléter)"""

FILLS = """.fill { display: inline-block; border-bottom: 1px dotted currentColor; opacity-x: 1; min-height: 8px; vertical-align: bottom; }
.f-xs { width: 52px; } .f-s { width: 88px; } .f-m { width: 130px; } .f-l { width: 185px; } .f-xl { width: 240px; }"""

BASE = """* { margin:0; padding:0; box-sizing:border-box; }
body { font-size: 9.6px; line-height: 1.5; }
sup { font-size: 6px; }
.row { display:flex; gap:10px; }
.half { flex:1; }
.vgrid { width:100%; border-collapse:collapse; }
.vgrid td { padding:2.2px 0; vertical-align:top; }
.vgrid .k { width:44%; padding-right:8px; }
table.items { width:100%; border-collapse:collapse; }
table.items th.num, table.items td.num { text-align:right; }
table.items th.qty, table.items td.qty { text-align:center; width:42px; }
table.items td.pos { width:22px; }
.pay-meta { display:flex; justify-content:space-between; margin-bottom:3px; }
.sigs { display:flex; gap:10px; }
.sig { flex:1; height:72px; padding:8px 11px; }
"""

# ================================================================ TEMPLATE C
# Covoiturage / startup — teal & coral, rounded, pill badges
C = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:10mm 12mm 8mm 12mm; }}
{BASE}{FILLS}
:root {{ --teal:#00b8a9; --coral:#ff6b6b; --ink:#243b4a; --soft:#e8f8f6; --softc:#fff0f0; --line:#d4ece9; --muted:#7d95a3; }}
body {{ font-family:"Poppins","Liberation Sans",sans-serif; color:var(--ink); }}
.fill {{ border-bottom-color:#9fc3bd; }}
.hero {{ background:linear-gradient(120deg,var(--teal) 0%,#00cdbb 60%,var(--coral) 130%); border-radius:16px; color:#fff; padding:12px 16px; display:flex; justify-content:space-between; align-items:center; }}
.hero .brand {{ font-weight:600; font-size:17px; }}
.hero .brand small {{ display:block; font-weight:300; font-size:8.4px; letter-spacing:2px; text-transform:uppercase; opacity:.9; }}
.hero .doc {{ text-align:right; font-weight:600; font-size:12px; }}
.hero .doc small {{ display:block; font-weight:300; font-size:8.4px; opacity:.92; margin-top:2px; }}
.hero .doc .fill {{ border-bottom-color:#ffffffaa; }}
.pill {{ display:inline-block; background:#ffffff26; border:1px solid #ffffff55; border-radius:99px; padding:1px 9px; font-size:7.6px; letter-spacing:1px; text-transform:uppercase; margin-top:3px; }}
.card {{ border:1.5px solid var(--line); border-radius:14px; padding:8px 12px; margin-top:8px; background:#fff; }}
.card.tint {{ background:var(--soft); border-color:transparent; }}
.card.tintc {{ background:var(--softc); border-color:transparent; }}
.card h2 {{ font-size:9px; font-weight:600; text-transform:uppercase; letter-spacing:1.4px; color:var(--teal); margin-bottom:4px; }}
.card.tintc h2 {{ color:var(--coral); }}
.card p {{ margin-bottom:2.6px; }}
.vgrid .k {{ color:var(--muted); }}
.vgrid .v b {{ color:var(--teal); }}
table.items th {{ font-weight:600; font-size:8.2px; text-transform:uppercase; letter-spacing:1px; color:#fff; background:var(--ink); text-align:left; padding:5px 10px; }}
table.items th:first-child {{ border-radius:10px 0 0 0; }} table.items th:last-child {{ border-radius:0 10px 0 0; }}
table.items td {{ padding:4.2px 10px; border-bottom:1px solid var(--line); }}
table.items td.pos {{ color:var(--muted); }}
tr.discount td {{ color:var(--coral); font-style:italic; }}
tr.total td {{ background:var(--teal); color:#fff; font-weight:600; font-size:11px; padding:6.5px 10px; border-bottom:none; }}
tr.total td:first-child {{ border-radius:0 0 0 10px; }} tr.total td:last-child {{ border-radius:0 0 10px 0; font-size:13px; }}
tr.total td small {{ font-weight:300; font-size:7.8px; }}
tr.total .fill {{ border-bottom-color:#d5f4f0; }}
.sig {{ border:1.5px dashed var(--coral); border-radius:14px; background:#fff; }}
.sig h4 {{ font-weight:600; font-size:9.4px; text-transform:uppercase; letter-spacing:1px; color:var(--coral); }}
.sig p {{ font-size:8px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:9px 2px 5px 2px; }}
.footer {{ margin-top:9px; text-align:center; font-size:7.4px; color:var(--muted); line-height:1.5; border-top:1.5px solid var(--line); padding-top:5px; }}
.badge-row {{ display:flex; gap:6px; margin-top:6px; }}
.b {{ border-radius:99px; padding:2px 11px; font-size:7.6px; font-weight:600; letter-spacing:.8px; text-transform:uppercase; }}
.b1 {{ background:var(--soft); color:var(--teal); }} .b2 {{ background:var(--softc); color:var(--coral); }} .b3 {{ background:#eef2f5; color:var(--muted); }}
</style></head><body>

<div class="hero">
  <div class="brand">votre-startup.fr
    <small>La route, en mieux ▸</small>
    <span class="pill">Vente entre passionnés</span>
  </div>
  <div class="doc">Contrat de vente<br>Véhicule d'occasion
    <small>N° <span class="fill f-s"></span> — Date <span class="fill f-s"></span></small>
  </div>
</div>

<div class="badge-row"><span class="b b1">★ Contrôle technique OK</span><span class="b b2">▸ Livraison flexible</span><span class="b b3">● Paiement sécurisé</span></div>

<div class="row">
  <div class="card tint half"><h2>Vendeur</h2>{VENDEUR}</div>
  <div class="card tintc half"><h2>Acheteur</h2>{ACHETEUR}</div>
</div>

<div class="card"><h2>Le véhicule</h2><table class="vgrid">{VEHICULE}</table></div>

<div style="height:8px"></div>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">Total <small>— TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<div class="card tint"><h2>Paiement</h2>{PAIEMENT}</div>
<div class="card"><h2>Livraison</h2><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</body></html>"""

# ================================================================ TEMPLATE D
# Psychédélique — gradients magenta/orange, Lora display, groovy
D = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:9mm 11mm 8mm 11mm; }}
{BASE}{FILLS}
:root {{ --p1:#7b2ff7; --p2:#f107a3; --p3:#ff8a00; --p4:#ffd60a; --ink:#3a1d5e; --cream:#fffaf2; --muted:#9a7fb8; }}
body {{ font-family:"Liberation Sans",sans-serif; color:var(--ink); background:var(--cream); }}
h1,h2,h4,.disp {{ font-family:"Lora",serif; }}
.fill {{ border-bottom:1px dotted #c79ae0; }}
.hero {{ background:linear-gradient(115deg,var(--p1),var(--p2) 45%,var(--p3) 80%,var(--p4)); border-radius:22px 22px 60px 22px; color:#fff; padding:13px 18px; }}
.hero h1 {{ font-size:19px; font-style:italic; font-weight:700; letter-spacing:.5px; text-shadow:2px 2px 0 #00000030; }}
.hero .sub {{ font-size:8.6px; letter-spacing:3px; text-transform:uppercase; opacity:.95; margin-top:2px; }}
.hero .ref {{ font-size:8.8px; margin-top:5px; }}
.hero .fill {{ border-bottom-color:#ffffffaa; }}
.wavebar {{ height:5px; margin:7px 0; border-radius:99px; background:repeating-linear-gradient(90deg,var(--p1) 0 22px,var(--p2) 22px 44px,var(--p3) 44px 66px,var(--p4) 66px 88px); }}
.card {{ background:#fff; border:2px solid transparent; border-radius:16px; padding:8px 12px; margin-bottom:8px;
        background-image:linear-gradient(#fff,#fff),linear-gradient(120deg,var(--p1),var(--p2),var(--p3)); background-origin:border-box; background-clip:padding-box,border-box; }}
.card h2 {{ font-size:11px; font-style:italic; font-weight:700; color:var(--p2); border-left:4px solid var(--p3); padding-left:7px; margin-bottom:4px; }}
.card p {{ margin-bottom:2.6px; }}
.vgrid .k {{ color:var(--muted); }}
.vgrid .v b {{ color:var(--p1); }}
table.items th {{ font-family:"Lora"; font-style:italic; font-weight:700; font-size:9px; color:#fff; background:linear-gradient(90deg,var(--p1),var(--p2)); text-align:left; padding:5px 10px; }}
table.items th:first-child {{ border-radius:12px 0 0 0; }} table.items th:last-child {{ border-radius:0 12px 0 0; }}
table.items td {{ padding:4.2px 10px; border-bottom:1px dashed #e6c7f2; background:#fff; }}
table.items td.pos {{ color:var(--p3); font-weight:bold; }}
tr.discount td {{ color:var(--p2); font-style:italic; }}
tr.total {{ background:linear-gradient(90deg,var(--p3),var(--p4)); }}
tr.total td {{ background:transparent; color:var(--ink); font-family:"Lora"; font-style:italic; font-weight:700; font-size:11.5px; padding:6.5px 10px; border-bottom:none; }}
tr.total td:first-child {{ border-radius:0 0 0 12px; }} tr.total td:last-child {{ border-radius:0 0 12px 0; font-size:13.5px; }}
tr.total td small {{ font-family:"Liberation Sans"; font-style:normal; font-weight:normal; font-size:7.8px; }}
.sig {{ border:2px dashed var(--p2); border-radius:16px; background:#fff; }}
.sig h4 {{ font-style:italic; font-weight:700; font-size:10px; color:var(--p1); }}
.sig p {{ font-size:8px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:8px 2px 5px 2px; }}
.footer {{ margin-top:8px; text-align:center; font-size:7.4px; color:var(--muted); line-height:1.5; }}
.stars {{ text-align:center; font-size:9px; color:var(--p2); letter-spacing:8px; margin-top:3px; }}
</style></head><body>

<div class="hero">
  <h1>✦ Contrat de Vente Cosmique ✦</h1>
  <div class="sub">Véhicule d'occasion — bon pour la route, bon pour l'âme</div>
  <div class="ref">N° de contrat : <span class="fill f-s"></span> &nbsp;•&nbsp; Date : <span class="fill f-s"></span></div>
</div>
<div class="wavebar"></div>

<div class="row">
  <div class="card half"><h2>Le Vendeur</h2>{VENDEUR}</div>
  <div class="card half"><h2>L'Acheteur</h2>{ACHETEUR}</div>
</div>

<div class="card"><h2>La Machine — Renault Clio</h2><table class="vgrid">{VEHICULE}</table></div>

<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">Total <small>— TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>
<div style="height:8px"></div>

<div class="card"><h2>Paiement</h2>{PAIEMENT}</div>
<div class="card"><h2>Livraison</h2><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="stars">✦ ✦ ✦</div>
<div class="footer">{FOOTER}</div>
</body></html>"""

# ================================================================ TEMPLATE E
# Aérospatial — dark header, mono labels, mission-control minimalism
E = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:0; }}
{BASE}{FILLS}
:root {{ --black:#0b0d10; --steel:#8a93a3; --lline:#d7dce3; --ink:#1c2128; --accent:#d92b2b; --panel:#f4f6f8; }}
body {{ font-family:"Liberation Sans",sans-serif; color:var(--ink); }}
.mono {{ font-family:"DejaVu Sans Mono",monospace; }}
.fill {{ border-bottom:1px dotted #a7b0bd; }}
.hero {{ background:var(--black); color:#fff; padding:11mm 13mm 7mm 13mm; }}
.hero .top {{ display:flex; justify-content:space-between; align-items:flex-start; }}
.hero h1 {{ font-family:"DejaVu Sans Mono"; font-size:15px; letter-spacing:4px; }}
.hero .sub {{ font-family:"DejaVu Sans Mono"; font-size:7.6px; letter-spacing:2.5px; color:var(--steel); margin-top:3px; text-transform:uppercase; }}
.hero .mission {{ text-align:right; font-family:"DejaVu Sans Mono"; font-size:7.8px; color:var(--steel); line-height:1.7; }}
.hero .mission b {{ color:#fff; font-weight:normal; }}
.hero .fill {{ border-bottom-color:#5a6472; }}
.hero .rule {{ height:1px; background:#2a2f38; margin-top:7px; }}
.hero .stat {{ display:flex; gap:26px; margin-top:6px; font-family:"DejaVu Sans Mono"; font-size:7.4px; letter-spacing:1.5px; color:var(--steel); text-transform:uppercase; }}
.hero .stat b {{ color:#fff; font-weight:normal; }}
.content {{ padding:6mm 13mm 7mm 13mm; }}
h2.sec {{ font-family:"DejaVu Sans Mono"; font-size:8.4px; letter-spacing:3px; text-transform:uppercase; color:var(--ink); margin:9px 0 4px 0; }}
h2.sec::before {{ content:"// "; color:var(--accent); }}
.panel {{ background:var(--panel); border-left:2px solid var(--black); padding:7px 11px; }}
.panel p {{ margin-bottom:2.6px; }}
.vgrid .k {{ font-family:"DejaVu Sans Mono"; font-size:7.6px; color:var(--steel); text-transform:uppercase; letter-spacing:.5px; }}
.vgrid .v b {{ color:var(--black); }}
table.items th {{ font-family:"DejaVu Sans Mono"; font-size:7.6px; letter-spacing:1.5px; text-transform:uppercase; color:var(--steel); text-align:left; padding:4px 9px; border-top:1.5px solid var(--black); border-bottom:1px solid var(--lline); }}
table.items td {{ padding:4px 9px; border-bottom:1px solid var(--lline); }}
table.items td.pos {{ font-family:"DejaVu Sans Mono"; color:var(--steel); }}
tr.discount td {{ color:var(--steel); font-style:italic; }}
tr.total td {{ border-top:1.5px solid var(--black); border-bottom:1.5px solid var(--black); font-family:"DejaVu Sans Mono"; font-size:11px; padding:6px 9px; }}
tr.total td:last-child {{ color:var(--accent); font-size:12.5px; }}
tr.total td small {{ font-size:7.4px; color:var(--steel); }}
.sig {{ border:1px solid var(--lline); background:#fff; position:relative; }}
.sig::before {{ content:"SIGNATURE"; position:absolute; right:8px; top:6px; font-family:"DejaVu Sans Mono"; font-size:6.6px; letter-spacing:2px; color:var(--lline); }}
.sig h4 {{ font-family:"DejaVu Sans Mono"; font-size:8.6px; letter-spacing:2px; text-transform:uppercase; }}
.sig p {{ font-size:7.8px; color:var(--steel); margin-top:2px; }}
.sig-intro {{ margin:9px 1px 5px 1px; }}
.footer {{ margin-top:9px; border-top:1px solid var(--lline); padding-top:5px; text-align:center; font-family:"DejaVu Sans Mono"; font-size:6.6px; letter-spacing:.5px; color:var(--steel); line-height:1.7; }}
</style></head><body>

<div class="hero">
  <div class="top">
    <div>
      <h1>CONTRAT DE VENTE</h1>
      <div class="sub">Véhicule d'occasion — protocole de transfert</div>
    </div>
    <div class="mission">
      MISSION : <b>CLIO-01</b><br>
      N° CONTRAT : <b><span class="fill f-s"></span></b><br>
      DATE : <b><span class="fill f-s"></span></b>
    </div>
  </div>
  <div class="rule"></div>
  <div class="stat"><span>VÉHICULE : <b>RENAULT CLIO 1.0 SCE</b></span><span>POUSSÉE : <b>72 CH / 53 KW</b></span><span>CARBURANT : <b>ESSENCE</b></span><span>STATUT : <b>GO</b></span></div>
</div>

<div class="content">

<div class="row">
  <div class="half"><h2 class="sec">Vendeur</h2><div class="panel">{VENDEUR}</div></div>
  <div class="half"><h2 class="sec">Acheteur</h2><div class="panel">{ACHETEUR}</div></div>
</div>

<h2 class="sec">Paramètres du véhicule</h2>
<div class="panel"><table class="vgrid">{VEHICULE}</table></div>

<h2 class="sec">Manifeste — produits et services</h2>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">TOTAL <small>— TVA INCLUSE (SELON RÉGIME APPLICABLE)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<h2 class="sec">Paiement — transfert de fonds</h2>
<div class="panel">{PAIEMENT}</div>

<h2 class="sec">T-0 : Livraison</h2>
<div class="panel"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</div>
</body></html>"""

# ================================================================ TEMPLATE F
# USA 250 — stars & stripes, navy/red/gold, semiquincentennial seal
F = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:9mm 12mm 8mm 12mm; }}
{BASE}{FILLS}
:root {{ --navy:#12294f; --red:#b31942; --gold:#c9a227; --cream:#fdfbf5; --line:#dfd9c8; --muted:#7a7f8c; }}
body {{ font-family:"Liberation Sans",sans-serif; color:#22273a; background:var(--cream); }}
h1,h2,h4 {{ font-family:"Lora",serif; }}
.fill {{ border-bottom:1px dotted #b9b2a0; }}
.flagwm {{ position:fixed; top:96mm; left:14mm; width:182mm; height:96mm; transform:rotate(-6deg); z-index:-1; opacity:0.5; background-image:url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%201235%20650%22%3E%3Crect%20x%3D%220%22%20y%3D%220%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23c9c9c9%22/%3E%3Crect%20x%3D%220%22%20y%3D%2250%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23ffffff%22/%3E%3Crect%20x%3D%220%22%20y%3D%22100%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23c9c9c9%22/%3E%3Crect%20x%3D%220%22%20y%3D%22150%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23ffffff%22/%3E%3Crect%20x%3D%220%22%20y%3D%22200%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23c9c9c9%22/%3E%3Crect%20x%3D%220%22%20y%3D%22250%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23ffffff%22/%3E%3Crect%20x%3D%220%22%20y%3D%22300%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23c9c9c9%22/%3E%3Crect%20x%3D%220%22%20y%3D%22350%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23ffffff%22/%3E%3Crect%20x%3D%220%22%20y%3D%22400%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23c9c9c9%22/%3E%3Crect%20x%3D%220%22%20y%3D%22450%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23ffffff%22/%3E%3Crect%20x%3D%220%22%20y%3D%22500%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23c9c9c9%22/%3E%3Crect%20x%3D%220%22%20y%3D%22550%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23ffffff%22/%3E%3Crect%20x%3D%220%22%20y%3D%22600%22%20width%3D%221235%22%20height%3D%2250%22%20fill%3D%22%23c9c9c9%22/%3E%3Crect%20x%3D%220%22%20y%3D%220%22%20width%3D%22494%22%20height%3D%22350%22%20fill%3D%22%23b8b8b8%22/%3E%3Ctext%20x%3D%2241%22%20y%3D%2245%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22123%22%20y%3D%2245%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22205%22%20y%3D%2245%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22287%22%20y%3D%2245%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22369%22%20y%3D%2245%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22451%22%20y%3D%2245%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%2282%22%20y%3D%2280%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22164%22%20y%3D%2280%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22246%22%20y%3D%2280%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22328%22%20y%3D%2280%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22410%22%20y%3D%2280%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%2241%22%20y%3D%22115%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22123%22%20y%3D%22115%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22205%22%20y%3D%22115%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22287%22%20y%3D%22115%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22369%22%20y%3D%22115%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22451%22%20y%3D%22115%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%2282%22%20y%3D%22150%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22164%22%20y%3D%22150%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22246%22%20y%3D%22150%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22328%22%20y%3D%22150%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22410%22%20y%3D%22150%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%2241%22%20y%3D%22185%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22123%22%20y%3D%22185%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22205%22%20y%3D%22185%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22287%22%20y%3D%22185%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22369%22%20y%3D%22185%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22451%22%20y%3D%22185%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%2282%22%20y%3D%22220%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22164%22%20y%3D%22220%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22246%22%20y%3D%22220%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22328%22%20y%3D%22220%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22410%22%20y%3D%22220%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%2241%22%20y%3D%22255%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22123%22%20y%3D%22255%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22205%22%20y%3D%22255%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22287%22%20y%3D%22255%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22369%22%20y%3D%22255%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22451%22%20y%3D%22255%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%2282%22%20y%3D%22290%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22164%22%20y%3D%22290%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22246%22%20y%3D%22290%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22328%22%20y%3D%22290%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22410%22%20y%3D%22290%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%2241%22%20y%3D%22325%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22123%22%20y%3D%22325%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22205%22%20y%3D%22325%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22287%22%20y%3D%22325%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22369%22%20y%3D%22325%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3Ctext%20x%3D%22451%22%20y%3D%22325%22%20font-size%3D%2230%22%20fill%3D%22%23ffffff%22%20text-anchor%3D%22middle%22%3E%E2%98%85%3C/text%3E%3C/svg%3E'); background-size:100% 100%; }}
.stripes {{ height:9px; background:repeating-linear-gradient(90deg,var(--red) 0 26px,#fff 26px 52px); border:1px solid var(--line); border-radius:3px; }}
.hero {{ background:var(--navy); color:#fff; border-radius:6px; margin-top:5px; padding:11px 16px; display:flex; justify-content:space-between; align-items:center; position:relative; overflow:hidden; }}
.hero .starfield {{ position:absolute; left:8px; top:4px; color:#ffffff2e; font-size:11px; letter-spacing:6px; line-height:1.5; }}
.hero h1 {{ font-size:17px; font-weight:700; letter-spacing:.5px; position:relative; }}
.hero .sub {{ font-size:8.4px; letter-spacing:2.6px; text-transform:uppercase; color:var(--gold); margin-top:2px; position:relative; }}
.hero .ref {{ font-size:8.6px; margin-top:4px; color:#d9def0; position:relative; }}
.hero .fill {{ border-bottom-color:#8fa0c9; }}
.seal {{ width:74px; height:74px; border-radius:50%; border:2.5px solid var(--gold); background:#0d1f3d; color:var(--gold); text-align:center; font-family:"Lora"; flex-shrink:0; padding-top:11px; position:relative; }}
.seal .n {{ font-size:21px; font-weight:700; line-height:1; }}
.seal .t {{ font-size:6.4px; letter-spacing:1.6px; text-transform:uppercase; margin-top:2px; }}
.seal .y {{ font-size:7.2px; margin-top:2px; color:#e8d48a; }}
.ribbon {{ text-align:center; margin:7px 0; }}
.ribbon span {{ display:inline-block; background:var(--red); color:#fff; font-family:"Lora"; font-weight:700; font-size:9.4px; letter-spacing:3px; text-transform:uppercase; padding:3.5px 26px; border-radius:3px; }}
.card {{ background:rgba(255,255,255,0.68); border:1px solid var(--line); border-radius:6px; padding:8px 12px; margin-bottom:8px; }}
.card h2 {{ font-size:10.5px; font-weight:700; color:var(--navy); border-bottom:2px solid var(--gold); display:inline-block; padding-bottom:1px; margin-bottom:4px; }}
.card h2::before {{ content:"★ "; color:var(--red); font-size:8.6px; }}
.card p {{ margin-bottom:2.6px; }}
.vgrid .k {{ color:var(--muted); }}
.vgrid .v b {{ color:var(--navy); }}
table.items th {{ font-family:"Lora"; font-weight:700; font-size:8.8px; color:#fff; background:var(--navy); text-align:left; padding:4.5px 10px; letter-spacing:.5px; }}
table.items th:first-child {{ border-radius:5px 0 0 0; }} table.items th:last-child {{ border-radius:0 5px 0 0; }}
table.items td {{ padding:4.2px 10px; border-bottom:1px solid var(--line); background:rgba(255,255,255,0.68); }}
table.items tr:nth-child(odd) td {{ background:rgba(247,244,234,0.7); }}
table.items td.pos {{ color:var(--red); font-weight:bold; }}
tr.discount td {{ color:var(--red); font-style:italic; }}
tr.total td {{ background:var(--red) !important; color:#fff; font-family:"Lora"; font-weight:700; font-size:11px; padding:6px 10px; border-bottom:none; }}
tr.total td:first-child {{ border-radius:0 0 0 5px; }} tr.total td:last-child {{ border-radius:0 0 5px 0; font-size:13px; }}
tr.total td small {{ font-family:"Liberation Sans"; font-weight:normal; font-size:7.6px; }}
tr.total .fill {{ border-bottom-color:#f2c4d0; }}
.sig {{ border:1.5px solid var(--navy); border-radius:6px; background:rgba(255,255,255,0.72); }}
.sig h4 {{ font-weight:700; font-size:9.6px; color:var(--navy); }}
.sig h4::before {{ content:"★ "; color:var(--gold); }}
.sig p {{ font-size:8px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:8px 2px 5px 2px; }}
.footer {{ margin-top:8px; text-align:center; font-size:7.4px; color:var(--muted); line-height:1.5; border-top:1px solid var(--line); padding-top:5px; }}
</style></head><body>

<div class="flagwm"></div>
<div class="stripes"></div>
<div class="hero">
  <div class="starfield">★ ★ ★ ★ ★<br>★ ★ ★ ★</div>
  <div>
    <h1>Contrat de Vente — Véhicule d'Occasion</h1>
    <div class="sub">Édition Semiquincentennial ★ 1776 – 2026 ★ Liberty Motors Edition</div>
    <div class="ref">N° de contrat : <span class="fill f-s"></span> &nbsp;•&nbsp; Date : <span class="fill f-s"></span></div>
  </div>
  <div class="seal"><div class="n">250</div><div class="t">Years of<br>Freedom</div><div class="y">1776 ★ 2026</div></div>
</div>
<div class="ribbon"><span>★ MAGA FOREVER ★ GREAT DEALS ONLY ★</span></div>

<div class="row">
  <div class="card half"><h2>Vendeur</h2>{VENDEUR}</div>
  <div class="card half"><h2>Acheteur</h2>{ACHETEUR}</div>
</div>

<div class="card"><h2>Le véhicule — Renault Clio</h2><table class="vgrid">{VEHICULE}</table></div>

<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">Total <small>— TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>
<div style="height:8px"></div>

<div class="card"><h2>Paiement</h2>{PAIEMENT}</div>
<div class="card"><h2>Livraison</h2><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</body></html>"""

# ---------------------------------------------------------------- render
for name, html in [("c_startup", C), ("d_psychedelique", D), ("e_aerospatial", E), ("f_usa250", F)]:
    open(f"version_{name}.html", "w").write(html)
    HTML(string=html, base_url=".").write_pdf(f"version_{name}.pdf")
    print(name, "ok")
