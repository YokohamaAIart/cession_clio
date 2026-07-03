#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Templates J (Plan de Vol), K (Menu Gastronomique), L (Une de Journal)."""
import gen_fun as gf
from weasyprint import HTML

VENDEUR, ACHETEUR, VEHICULE, ITEMS = gf.VENDEUR, gf.ACHETEUR, gf.VEHICULE, gf.ITEMS
PAIEMENT, LIVRAISON, SIGNATURES, FOOTER = gf.PAIEMENT, gf.LIVRAISON, gf.SIGNATURES, gf.FOOTER
BASE, FILLS = gf.BASE, gf.FILLS

# ================================================================ TEMPLATE J
# Plan de Vol — boarding pass, le contrat comme un vol VDR -> ACH
J = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:9mm 11mm 8mm 11mm; }}
{BASE}{FILLS}
:root {{ --navy:#0e2a47; --sky:#3fa7d6; --amber:#f5a623; --paper:#fdfdfd; --line:#d9e2ec; --muted:#7b8ca0; }}
body {{ font-family:"Liberation Sans",sans-serif; font-size:9.4px; color:#22303f; background:var(--paper); }}
.mono {{ font-family:"DejaVu Sans Mono",monospace; }}
.fill {{ border-bottom:1px dotted #a9b8c8; }}
.pass {{ border:1.5px solid var(--navy); border-radius:12px; overflow:hidden; display:flex; }}
.pass .main {{ flex:1; }}
.pass .stub {{ width:44mm; border-left:2px dashed var(--navy); background:#eef5fb; padding:8px 10px; font-family:"DejaVu Sans Mono"; font-size:7.4px; color:var(--navy); line-height:1.9; }}
.pass .stub b {{ font-size:9px; }}
.passhead {{ background:var(--navy); color:#fff; padding:7px 13px; display:flex; justify-content:space-between; align-items:center; }}
.passhead .t {{ font-family:"DejaVu Sans Mono"; font-size:11.5px; letter-spacing:2.5px; }}
.passhead .t small {{ display:block; font-size:7px; letter-spacing:2px; color:#9fc3e8; margin-top:2px; }}
.passhead .vol {{ font-family:"DejaVu Sans Mono"; font-size:8.2px; text-align:right; color:#cfe3f6; line-height:1.7; }}
.passhead .vol b {{ color:var(--amber); font-weight:normal; }}
.route {{ display:flex; align-items:center; gap:14px; padding:6px 13px 5px 13px; }}
.route .code {{ font-family:"DejaVu Sans Mono"; font-size:23px; font-weight:bold; color:var(--navy); }}
.route .city {{ font-size:7.6px; text-transform:uppercase; letter-spacing:1.5px; color:var(--muted); }}
.route .plane {{ flex:1; text-align:center; color:var(--sky); font-size:13px; position:relative; }}
.route .plane::before, .route .plane::after {{ content:""; display:inline-block; width:34%; border-top:1.5px dashed var(--sky); vertical-align:middle; margin:0 5px; }}
.infobar {{ display:flex; gap:0; border-top:1px solid var(--line); }}
.infobar div {{ flex:1; padding:4px 13px; border-right:1px solid var(--line); }}
.infobar div:last-child {{ border-right:none; }}
.infobar .l {{ font-family:"DejaVu Sans Mono"; font-size:6.6px; letter-spacing:1.5px; color:var(--muted); text-transform:uppercase; }}
.infobar .v {{ font-size:9px; font-weight:bold; color:var(--navy); }}
h2.sec {{ font-family:"DejaVu Sans Mono"; font-size:8.6px; letter-spacing:2.5px; text-transform:uppercase; color:var(--navy); margin:6.5px 0 3px 0; }}
h2.sec::before {{ content:"▸ "; color:var(--amber); }}
.panel {{ background:#f4f8fc; border:1px solid var(--line); border-radius:8px; padding:6px 12px; }}
.panel p {{ margin-bottom:2.6px; }}
.vgrid .k {{ color:var(--muted); }}
.vgrid .v b {{ color:var(--navy); }}
table.items th {{ font-family:"DejaVu Sans Mono"; font-size:7.4px; letter-spacing:1.5px; text-transform:uppercase; color:#fff; background:var(--sky); text-align:left; padding:4px 10px; }}
table.items th:first-child {{ border-radius:8px 0 0 0; }} table.items th:last-child {{ border-radius:0 8px 0 0; }}
table.items td {{ padding:4px 10px; border-bottom:1px solid var(--line); background:#fff; }}
table.items td.pos {{ font-family:"DejaVu Sans Mono"; color:var(--muted); }}
tr.discount td {{ color:var(--amber); font-style:italic; }}
tr.total td {{ background:var(--navy); color:#fff; font-family:"DejaVu Sans Mono"; font-size:10.5px; padding:6px 10px; border-bottom:none; }}
tr.total td:first-child {{ border-radius:0 0 0 8px; }} tr.total td:last-child {{ border-radius:0 0 8px 0; color:var(--amber); font-size:12px; }}
tr.total td small {{ font-size:7px; color:#9fc3e8; }}
tr.total .fill {{ border-bottom-color:#6d89a8; }}
.sig {{ border:1.5px solid var(--navy); border-radius:8px; background:#fff; position:relative; }}
.sig::after {{ content:"EMBARQUEMENT VALIDÉ"; position:absolute; right:9px; bottom:7px; font-family:"DejaVu Sans Mono"; font-size:6.2px; letter-spacing:1.5px; color:var(--line); border:1px solid var(--line); border-radius:3px; padding:1px 5px; }}
.sig h4 {{ font-family:"DejaVu Sans Mono"; font-size:8.8px; letter-spacing:1.5px; text-transform:uppercase; color:var(--navy); }}
.sig p {{ font-size:7.6px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:9px 1px 5px 1px; }}
.footer {{ margin-top:8px; text-align:center; font-size:7px; color:var(--muted); line-height:1.6; border-top:1px solid var(--line); padding-top:5px; }}
.sig {{ height:62px; }}
.footer {{ margin-top:6px; }}
.barcode {{ margin-top:6px; height:26px; background:repeating-linear-gradient(90deg,var(--navy) 0px,var(--navy) 2px,#eef5fb 2px,#eef5fb 4px,var(--navy) 4px,var(--navy) 5px,#eef5fb 5px,#eef5fb 9px,var(--navy) 9px,var(--navy) 12px,#eef5fb 12px,#eef5fb 14px); border-radius:2px; }}
</style></head><body>

<div class="pass">
  <div class="main">
    <div class="passhead">
      <div class="t">PLAN DE VOL — CONTRAT DE VENTE<small>VÉHICULE D'OCCASION — TRANSFERT DE PROPRIÉTÉ</small></div>
      <div class="vol">VOL <b>CL-072</b> · PORTE <b>01</b> · CLASSE <b>CITADINE</b><br>N° CONTRAT <b><span class="fill f-s"></span></b> · DATE <b><span class="fill f-s"></span></b></div>
    </div>
    <div class="route">
      <div><div class="code">VDR</div><div class="city">Vendeur — Départ</div></div>
      <div class="plane">✈</div>
      <div style="text-align:right"><div class="code">ACH</div><div class="city">Acheteur — Arrivée</div></div>
    </div>
    <div class="infobar">
      <div><div class="l">Appareil</div><div class="v">Renault Clio 1.0 SCe</div></div>
      <div><div class="l">Poussée</div><div class="v">72 ch / 53 kW</div></div>
      <div><div class="l">Carburant</div><div class="v">Essence · Euro 6</div></div>
      <div><div class="l">Vitesse de croisière</div><div class="v">130 km/h (réglementaire)</div></div>
      <div><div class="l">Statut</div><div class="v">PRÊT AU DÉCOLLAGE</div></div>
    </div>
  </div>
  <div class="stub">
    <b>CL-072</b><br>
    SIÈGES : 5<br>
    PORTES : 5<br>
    BAGAGES : 300 L<br>
    CLÉS : 2<br>
    ALT. MAX : 0 FT<br>
    <div class="barcode"></div>
  </div>
</div>

<div class="row" style="margin-top:8px">
  <div class="half"><h2 class="sec">Commandant de bord — Vendeur</h2><div class="panel">{VENDEUR}</div></div>
  <div class="half"><h2 class="sec">Passager repreneur — Acheteur</h2><div class="panel">{ACHETEUR}</div></div>
</div>

<h2 class="sec">Fiche technique de l'appareil</h2>
<div class="panel"><table class="vgrid">{VEHICULE}</table></div>

<h2 class="sec">Manifeste de bord — Produits et services</h2>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">TOTAL <small>— TVA INCLUSE (SELON RÉGIME APPLICABLE)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<h2 class="sec">Clairance financière — Paiement</h2>
<div class="panel">{PAIEMENT}</div>

<h2 class="sec">Atterrissage — Livraison</h2>
<div class="panel"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</body></html>"""

# ================================================================ TEMPLATE K
# Menu Gastronomique — le contrat servi en menu dégustation
K = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:8mm 14mm 7mm 14mm; }}
{BASE}{FILLS}
:root {{ --bord:#6b1f2e; --gold:#b98d3c; --cream:#fdfaf3; --line:#e6d9c3; --muted:#95866f; }}
body {{ font-family:"Liberation Sans",sans-serif; font-size:9.4px; color:#3a2e26; background:var(--cream); }}
h1,h2,h4,.it {{ font-family:"Lora",serif; }}
.fill {{ border-bottom:1px dotted #c4b394; }}
.hero {{ text-align:center; padding-bottom:6px; border-bottom:1px solid var(--gold); }}
.hero .resto {{ font-size:8.4px; letter-spacing:5px; text-transform:uppercase; color:var(--gold); }}
.hero h1 {{ font-family:"Lora"; font-style:italic; font-size:21px; font-weight:700; color:var(--bord); margin:2px 0 0 0; }}
.hero .sub {{ font-family:"Lora"; font-style:italic; font-size:9.6px; color:var(--muted); margin-top:1px; }}
.hero .ref {{ font-size:8.4px; color:var(--muted); margin-top:4px; }}
.hero .etoiles {{ color:var(--gold); font-size:9px; letter-spacing:5px; margin-top:2px; }}
.course {{ text-align:center; margin:8px 0 3.5px 0; }}
.course h2 {{ display:inline; font-family:"Lora"; font-style:italic; font-size:12px; font-weight:700; color:var(--bord); }}
.course .svc {{ display:block; font-size:7px; letter-spacing:3px; text-transform:uppercase; color:var(--gold); margin-bottom:1px; }}
.panel {{ background:#fffefa; border:1px solid var(--line); padding:7px 13px; }}
.panel p {{ margin-bottom:2.6px; }}
.vgrid .k {{ color:var(--muted); }}
.vgrid .v b {{ color:var(--bord); }}
table.items {{ }}
table.items th {{ font-family:"Lora"; font-style:italic; font-weight:700; font-size:9px; color:var(--bord); background:none; border-top:1px solid var(--gold); border-bottom:1px solid var(--gold); text-align:left; padding:4px 10px; }}
table.items td {{ padding:4.2px 10px; border-bottom:1px dotted var(--line); background:none; }}
table.items td.pos {{ color:var(--gold); font-family:"Lora"; }}
tr.discount td {{ color:var(--muted); font-style:italic; }}
tr.total td {{ border-top:1.5px solid var(--bord); border-bottom:1.5px double var(--bord); font-family:"Lora"; font-style:italic; font-weight:700; font-size:11.5px; color:var(--bord); padding:6px 10px; }}
tr.total td:last-child {{ font-size:13px; }}
tr.total td small {{ font-family:"Liberation Sans"; font-style:normal; font-weight:normal; font-size:7.4px; color:var(--muted); }}
.sig {{ border:1px solid var(--gold); background:#fffefa; }}
.sig h4 {{ font-style:italic; font-weight:700; font-size:10px; color:var(--bord); }}
.sig p {{ font-size:7.8px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:8px 2px 5px 2px; text-align:center; font-style:italic; font-family:"Lora"; }}
.footer {{ margin-top:8px; text-align:center; font-size:7.2px; color:var(--muted); line-height:1.6; border-top:1px solid var(--line); padding-top:5px; }}
.divider {{ text-align:center; color:var(--gold); font-size:8px; letter-spacing:6px; margin:5px 0 0 0; }}
</style></head><body>

<div class="hero">
  <div class="resto">La Table de l'Automobile</div>
  <h1>Menu Dégustation — Contrat de Vente</h1>
  <div class="sub">Véhicule d'occasion, servi sur une page — cuisson : lu et approuvé</div>
  <div class="etoiles">★ ★ ★</div>
  <div class="ref">N° de contrat : <span class="fill f-s"></span> &nbsp;•&nbsp; Date du service : <span class="fill f-s"></span></div>
</div>

<div class="row" style="margin-top:6px">
  <div class="half"><div class="course"><span class="svc">Mise en bouche</span><h2>Le Vendeur, maison</h2></div><div class="panel">{VENDEUR}</div></div>
  <div class="half"><div class="course"><span class="svc">En accompagnement</span><h2>L'Acheteur, de saison</h2></div><div class="panel">{ACHETEUR}</div></div>
</div>

<div class="course"><span class="svc">Plat signature</span><h2>Renault Clio 1.0 SCe, élevée sur route, jus de 72 ch</h2></div>
<div class="panel"><table class="vgrid">{VEHICULE}</table></div>

<div class="course"><span class="svc">La carte</span><h2>Produits et services</h2></div>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">L'addition <small>— TVA incluse (selon régime applicable), service compris</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<div class="course"><span class="svc">Accord mets &amp; virements</span><h2>Le Paiement</h2></div>
<div class="panel">{PAIEMENT}</div>

<div class="course"><span class="svc">Le café gourmand</span><h2>La Livraison</h2></div>
<div class="panel"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="divider">❦</div>
<div class="footer">{FOOTER}</div>
</body></html>"""

# ================================================================ TEMPLATE L
# Une de Journal 1900 — LA GAZETTE DE L'AUTOMOBILE : VENDU !
L = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:8mm 11mm 7mm 11mm; }}
{BASE}{FILLS}
:root {{ --ink:#1c1a17; --paper:#f4efe3; --line:#c9c0ab; --muted:#6f6a5c; --rouge:#8f2a1e; }}
body {{ font-family:"DejaVu Serif",serif; font-size:9.2px; color:var(--ink); background:var(--paper); }}
.fill {{ border-bottom:1px dotted #9d947d; }}
.masthead {{ text-align:center; border-bottom:3.5px double var(--ink); padding-bottom:5px; }}
.masthead .over {{ display:flex; justify-content:space-between; font-size:7.4px; text-transform:uppercase; letter-spacing:1.5px; color:var(--muted); border-bottom:1px solid var(--line); padding-bottom:2px; margin-bottom:3px; }}
.masthead h1 {{ font-family:"DejaVu Serif"; font-weight:bold; font-size:26px; letter-spacing:2px; }}
.masthead .devise {{ font-style:italic; font-size:8.2px; color:var(--muted); margin-top:1px; }}
.headline {{ text-align:center; border-bottom:1.5px solid var(--ink); padding:5px 0 4px 0; }}
.headline h2 {{ font-size:16.5px; font-weight:bold; letter-spacing:1px; text-transform:uppercase; }}
.headline h2 .r {{ color:var(--rouge); }}
.headline .lede {{ font-style:italic; font-size:9px; color:var(--muted); margin-top:2px; }}
h3.col {{ font-size:9.8px; font-weight:bold; text-transform:uppercase; letter-spacing:1px; text-align:center; border-top:1px solid var(--ink); border-bottom:1px solid var(--ink); padding:2px 0; margin:7px 0 4px 0; }}
.panel {{ padding:0 2px; }}
.panel p {{ margin-bottom:2.6px; }}
.rule {{ border-bottom:1px solid var(--line); margin:5px 0; }}
.vgrid .k {{ color:var(--muted); font-style:italic; }}
.vgrid .v b {{ font-weight:bold; }}
table.items {{ border-top:1.5px solid var(--ink); }}
table.items th {{ font-size:8.2px; font-weight:bold; text-transform:uppercase; letter-spacing:1px; border-bottom:1px solid var(--ink); text-align:left; padding:3.5px 8px; }}
table.items td {{ padding:3.8px 8px; border-bottom:1px dotted var(--line); }}
table.items td.pos {{ color:var(--muted); }}
tr.discount td {{ font-style:italic; color:var(--rouge); }}
tr.total td {{ border-top:1.5px solid var(--ink); border-bottom:3px double var(--ink); font-weight:bold; font-size:11px; padding:5px 8px; }}
tr.total td:last-child {{ color:var(--rouge); font-size:12.5px; }}
tr.total td small {{ font-weight:normal; font-size:7.2px; font-style:italic; color:var(--muted); }}
.annonce {{ border:1.5px solid var(--ink); padding:6px 11px; margin-top:6px; background:#faf6ea; }}
.annonce h4 {{ font-size:9.4px; font-weight:bold; text-transform:uppercase; letter-spacing:1px; text-align:center; border-bottom:1px solid var(--line); padding-bottom:2px; margin-bottom:3px; }}
.annonce p {{ margin-bottom:2.4px; }}
.sig {{ border:1px solid var(--ink); background:#faf6ea; }}
.sig h4 {{ font-size:9.2px; font-weight:bold; text-transform:uppercase; letter-spacing:1px; }}
.sig p {{ font-size:7.6px; font-style:italic; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:7px 1px 4px 1px; font-style:italic; }}
.footer {{ margin-top:7px; text-align:center; font-size:7px; font-style:italic; color:var(--muted); line-height:1.6; border-top:3px double var(--ink); padding-top:4px; }}
.twocol {{ display:flex; gap:12px; }}
.twocol .c {{ flex:1; }}
.vsep {{ width:1px; background:var(--line); }}
</style></head><body>

<div class="masthead">
  <div class="over"><span>N° de contrat : <span class="fill f-xs"></span></span><span>Édition spéciale — Une page, un propriétaire</span><span>Date : <span class="fill f-s"></span></span></div>
  <h1>LA GAZETTE DE L'AUTOMOBILE</h1>
  <div class="devise">« Tout véhicule mérite une seconde route » — Fondée à l'ère du moteur à explosion</div>
</div>

<div class="headline">
  <h2><span class="r">VENDU !</span> — UNE RENAULT CLIO CHANGE DE MAINS</h2>
  <div class="lede">Notre correspondant rapporte la cession en bonne et due forme d'une Clio 1.0 SCe de 72 chevaux. Les parties ont signé. La foule est en liesse.</div>
</div>

<div class="twocol" style="margin-top:5px">
  <div class="c">
    <h3 class="col">Le Cédant — Vendeur</h3>
    <div class="panel">{VENDEUR}</div>
  </div>
  <div class="vsep"></div>
  <div class="c">
    <h3 class="col">Le Repreneur — Acheteur</h3>
    <div class="panel">{ACHETEUR}</div>
  </div>
</div>

<h3 class="col">Portrait de la Machine — Les Faits, Rien que les Faits</h3>
<div class="panel"><table class="vgrid">{VEHICULE}</table></div>

<h3 class="col">Cours &amp; Cotations — Produits et Services</h3>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">Total <small>— TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<div class="annonce">
  <h4>Avis de Paiement — Rubrique Officielle</h4>
  {PAIEMENT}
</div>

<div class="annonce">
  <h4>Petites Annonces — Livraison</h4>
  <p>{LIVRAISON}</p>
</div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</body></html>"""

for name, html in [("j_plan_de_vol", J), ("k_menu_gastro", K), ("l_gazette", L)]:
    open(f"version_{name}.html", "w").write(html)
    HTML(string=html, base_url=".").write_pdf(f"version_{name}.pdf")
    print(name, "ok")
