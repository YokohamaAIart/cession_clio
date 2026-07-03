#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Templates N (Atelier sobre) & O (Blueprint) — garage/mechanic look, crown+car watermark."""
import urllib.parse
import gen_fun as gf
from weasyprint import HTML

VENDEUR, ACHETEUR, VEHICULE, ITEMS = gf.VENDEUR, gf.ACHETEUR, gf.VEHICULE, gf.ITEMS
PAIEMENT, LIVRAISON, SIGNATURES, FOOTER = gf.PAIEMENT, gf.LIVRAISON, gf.SIGNATURES, gf.FOOTER
BASE, FILLS = gf.BASE, gf.FILLS

# --- original crown-over-hatchback silhouette (inspired by MGP identity, NOT a copy) ---
def car_svg(stroke, fill_op=0.0):
    return f"""<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 620 300'>
<g fill='none' stroke='{stroke}' stroke-width='5' stroke-linejoin='round' stroke-linecap='round'>
<!-- crown -->
<path d='M232 70 L250 34 L288 60 L310 22 L332 60 L370 34 L388 70 L232 70 Z'/>
<circle cx='250' cy='34' r='6' fill='{stroke}'/><circle cx='310' cy='22' r='6' fill='{stroke}'/><circle cx='370' cy='34' r='6' fill='{stroke}'/>
<line x1='232' y1='82' x2='388' y2='82'/>
<!-- hatchback body -->
<path d='M60 232 L92 232 M528 232 L560 232'/>
<path d='M78 232 C78 210 96 196 118 196 L150 196 L196 150 C206 140 220 134 236 134 L392 134 C410 134 428 142 440 156 L474 196 L508 200 C532 204 548 222 548 232'/>
<path d='M78 232 L548 232'/>
<!-- windows -->
<path d='M204 158 L232 134 M300 134 L300 190 M300 190 L172 190 L204 158 M392 134 L392 190 L300 190'/>
<!-- wheels -->
<circle cx='176' cy='234' r='40'/><circle cx='176' cy='234' r='16'/>
<circle cx='452' cy='234' r='40'/><circle cx='452' cy='234' r='16'/>
<!-- ground -->
<line x1='30' y1='276' x2='590' y2='276' stroke-dasharray='2 14'/>
</g></svg>"""

wm_gray = "data:image/svg+xml," + urllib.parse.quote(car_svg("#7a7f86"))
wm_blue = "data:image/svg+xml," + urllib.parse.quote(car_svg("#5b7c99"))

# ================================================================ TEMPLATE N
# Atelier — steel gray, oil-stain warmth, monospace tags, near-monochrome
N = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:0; }}
{BASE}{FILLS}
:root {{ --steel:#2b2f36; --steel2:#3d434c; --oil:#8a6d3b; --grease:#c8933b; --paper:#f4f2ee; --panel:#eceae4; --line:#cfccc3; --ink:#26292e; --muted:#7c7970; }}
body {{ font-family:"Liberation Sans",sans-serif; font-size:9.4px; color:var(--ink); background:var(--paper); }}
.mono {{ font-family:"DejaVu Sans Mono",monospace; }}
.fill {{ border-bottom:1px dotted #a7a49b; }}
.carwm {{ position:fixed; top:118mm; left:38mm; width:134mm; height:65mm; z-index:-1; opacity:0.3;
  background-image:url('{wm_gray}'); background-size:100% 100%; }}
.sheet {{ padding:11mm 13mm 9mm 13mm; }}
/* header plate */
.plate {{ background:var(--steel); color:#e9e7e1; border:2px solid var(--steel); border-radius:3px; padding:8px 14px; display:flex; justify-content:space-between; align-items:center; }}
.plate .brand {{ font-family:"DejaVu Sans Mono"; font-weight:bold; font-size:15px; letter-spacing:2px; }}
.plate .brand small {{ display:block; font-family:"Liberation Sans"; font-weight:normal; font-size:7.4px; letter-spacing:2px; color:#a9a69d; margin-top:2px; text-transform:uppercase; }}
.plate .doc {{ text-align:right; font-family:"DejaVu Sans Mono"; font-size:8.4px; color:#cbc8bf; line-height:1.7; }}
.plate .doc b {{ color:#e9e7e1; font-weight:normal; }}
.plate .doc .fill {{ border-bottom-color:#6a6e75; }}
.tapebar {{ height:5px; background:repeating-linear-gradient(45deg,var(--grease) 0 12px,var(--steel) 12px 24px); margin-top:3px; opacity:0.85; }}
/* sections */
h2.sec {{ font-family:"DejaVu Sans Mono"; font-size:8.4px; letter-spacing:2px; text-transform:uppercase; color:var(--steel); margin:9px 0 3.5px 0; border-bottom:1px solid var(--line); padding-bottom:2px; }}
h2.sec::before {{ content:"▪ "; color:var(--grease); }}
.panel {{ background:rgba(236,234,228,0.72); border:1px solid var(--line); border-left:3px solid var(--steel); padding:6px 11px; }}
.panel p {{ margin-bottom:2.4px; }}
.vgrid .k {{ font-family:"DejaVu Sans Mono"; font-size:7.6px; color:var(--muted); text-transform:uppercase; letter-spacing:.3px; }}
.vgrid .v b {{ color:var(--steel); }}
/* items */
table.items th {{ font-family:"DejaVu Sans Mono"; font-size:7.4px; letter-spacing:1.5px; text-transform:uppercase; color:#e9e7e1; background:var(--steel); text-align:left; padding:4px 10px; }}
table.items td {{ padding:4px 10px; border-bottom:1px solid var(--line); background:rgba(255,255,255,0.55); }}
table.items td.pos {{ font-family:"DejaVu Sans Mono"; color:var(--muted); }}
tr.discount td {{ color:var(--oil); font-style:italic; }}
tr.total td {{ background:var(--steel2); color:#e9e7e1; font-family:"DejaVu Sans Mono"; font-size:10.5px; padding:6px 10px; border-bottom:none; }}
tr.total td:last-child {{ color:var(--grease); font-size:12px; }}
tr.total td small {{ font-size:7px; color:#a9a69d; }}
tr.total .fill {{ border-bottom-color:#7a7f86; }}
/* signatures */
.sig {{ border:1px solid var(--line); background:rgba(236,234,228,0.72); position:relative; }}
.sig::after {{ content:"BON POUR ACCORD"; position:absolute; right:9px; bottom:7px; font-family:"DejaVu Sans Mono"; font-size:6.2px; letter-spacing:1.5px; color:var(--line); border:1px solid var(--line); padding:1px 5px; border-radius:2px; }}
.sig h4 {{ font-family:"DejaVu Sans Mono"; font-size:8.6px; letter-spacing:1.5px; text-transform:uppercase; color:var(--steel); }}
.sig p {{ font-size:7.6px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:9px 1px 5px 1px; }}
.footer {{ margin-top:8px; border-top:1px solid var(--line); padding-top:5px; text-align:center; font-family:"DejaVu Sans Mono"; font-size:6.6px; letter-spacing:.4px; color:var(--muted); line-height:1.7; }}
</style></head><body>
<div class="carwm"></div>
<div class="sheet">

<div class="plate">
  <div class="brand">GARAGE — VÉHICULE D'OCCASION<small>Contrat de vente · atelier mécanique</small></div>
  <div class="doc">N° CONTRAT <b><span class="fill f-s"></span></b><br>DATE <b><span class="fill f-s"></span></b></div>
</div>
<div class="tapebar"></div>

<div class="row" style="margin-top:8px">
  <div class="half"><h2 class="sec">Vendeur</h2><div class="panel">{VENDEUR}</div></div>
  <div class="half"><h2 class="sec">Acheteur</h2><div class="panel">{ACHETEUR}</div></div>
</div>

<h2 class="sec">Fiche technique du véhicule</h2>
<div class="panel"><table class="vgrid">{VEHICULE}</table></div>

<h2 class="sec">Bon de commande — produits &amp; prestations</h2>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">TOTAL <small>— TVA INCLUSE (SELON RÉGIME APPLICABLE)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<h2 class="sec">Règlement</h2>
<div class="panel">{PAIEMENT}</div>

<h2 class="sec">Remise du véhicule</h2>
<div class="panel"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</div>
</body></html>"""

# ================================================================ TEMPLATE O
# Blueprint — dark cyan technical drawing, grid, exploded-view feel
O = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:0; }}
{BASE}{FILLS}
:root {{ --bp:#12303f; --bp2:#1c4257; --cyan:#7fb2c9; --grid:#20465a; --paper:#e8eef1; --line:#b9c9d1; --ink:#1a2b33; --muted:#6b8593; }}
body {{ font-family:"DejaVu Sans Mono",monospace; font-size:9px; color:var(--ink); }}
.fill {{ border-bottom:1px dotted #8fa6b1; }}
.bg {{ position:fixed; inset:0; z-index:-2; background:var(--paper);
  background-image:linear-gradient(#d3dde2 1px,transparent 1px),linear-gradient(90deg,#d3dde2 1px,transparent 1px);
  background-size:6mm 6mm; }}
.carwm {{ position:fixed; top:120mm; left:40mm; width:130mm; height:63mm; z-index:-1; opacity:0.3;
  background-image:url('{wm_blue}'); background-size:100% 100%; }}
.sheet {{ padding:9mm 12mm 8mm 12mm; }}
/* title block bottom-right of engineering drawings, here on top */
.titleblock {{ border:2px solid var(--bp); background:rgba(232,238,241,0.85); }}
.tb-top {{ background:var(--bp); color:#dcebf1; padding:7px 13px; display:flex; justify-content:space-between; align-items:center; }}
.tb-top .brand {{ font-weight:bold; font-size:13px; letter-spacing:2px; }}
.tb-top .brand small {{ display:block; font-weight:normal; font-size:7px; letter-spacing:2px; color:#9dc0d0; margin-top:2px; }}
.tb-top .rev {{ text-align:right; font-size:7.6px; color:#bcd6e1; line-height:1.7; }}
.tb-top .rev b {{ color:#fff; font-weight:normal; }} .tb-top .fill {{ border-bottom-color:#4d7085; }}
.tb-grid {{ display:flex; }}
.tb-grid div {{ flex:1; padding:3.5px 10px; border-right:1px solid var(--line); font-size:7.4px; }}
.tb-grid div:last-child {{ border-right:none; }}
.tb-grid .l {{ color:var(--muted); text-transform:uppercase; letter-spacing:1px; font-size:6.6px; }}
.tb-grid .v {{ font-weight:bold; color:var(--bp); }}
h2.sec {{ font-size:8.2px; letter-spacing:2px; text-transform:uppercase; color:var(--bp); margin:8px 0 3px 0; }}
h2.sec::before {{ content:"◄ "; color:var(--cyan); }}
h2.sec::after {{ content:" ►"; color:var(--cyan); }}
.panel {{ background:rgba(232,238,241,0.8); border:1.2px solid var(--bp); padding:6px 11px; }}
.panel p {{ margin-bottom:2.4px; }}
.vgrid .k {{ color:var(--muted); text-transform:uppercase; font-size:7.4px; letter-spacing:.3px; }}
.vgrid .v b {{ color:var(--bp); }}
table.items th {{ font-size:7.2px; letter-spacing:1.5px; text-transform:uppercase; color:#dcebf1; background:var(--bp); text-align:left; padding:4px 10px; }}
table.items td {{ padding:4px 10px; border-bottom:1px solid var(--line); background:rgba(232,238,241,0.8); }}
table.items td.pos {{ color:var(--cyan); }}
tr.discount td {{ color:var(--muted); font-style:italic; }}
tr.total td {{ background:var(--bp2); color:#dcebf1; font-size:10px; padding:6px 10px; border-bottom:none; }}
tr.total td:last-child {{ color:#a9d4e6; font-size:11.5px; }}
tr.total td small {{ font-size:7px; color:#9dc0d0; }}
tr.total .fill {{ border-bottom-color:#5f8398; }}
.sig {{ border:1.2px solid var(--bp); background:rgba(232,238,241,0.8); position:relative; }}
.sig::after {{ content:"APPROVED / VALIDÉ"; position:absolute; right:9px; bottom:7px; font-size:6px; letter-spacing:1.5px; color:var(--line); border:1px solid var(--line); padding:1px 5px; }}
.sig h4 {{ font-size:8.4px; letter-spacing:1.5px; text-transform:uppercase; color:var(--bp); }}
.sig p {{ font-size:7.4px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:8px 1px 4px 1px; }}
.footer {{ margin-top:7px; border-top:1.2px solid var(--bp); padding-top:5px; text-align:center; font-size:6.4px; letter-spacing:.4px; color:var(--muted); line-height:1.7; }}
</style></head><body>
<div class="bg"></div>
<div class="carwm"></div>
<div class="sheet">

<div class="titleblock">
  <div class="tb-top">
    <div class="brand">CONTRAT DE VENTE<small>DWG — VÉHICULE D'OCCASION / USED VEHICLE</small></div>
    <div class="rev">DWG N° <b><span class="fill f-s"></span></b> · DATE <b><span class="fill f-s"></span></b><br>SCALE 1:1 · SHEET 1/1 · REV —</div>
  </div>
  <div class="tb-grid">
    <div><span class="l">Unit</span><br><span class="v">Renault Clio 1.0 SCe</span></div>
    <div><span class="l">Power</span><br><span class="v">72 ch / 53 kW</span></div>
    <div><span class="l">Fuel</span><br><span class="v">Essence · Euro 6</span></div>
    <div><span class="l">Material</span><br><span class="v">Acier / alu</span></div>
    <div><span class="l">Status</span><br><span class="v">FOR SALE</span></div>
  </div>
</div>

<div class="row" style="margin-top:8px">
  <div class="half"><h2 class="sec">Vendeur / Seller</h2><div class="panel">{VENDEUR}</div></div>
  <div class="half"><h2 class="sec">Acheteur / Buyer</h2><div class="panel">{ACHETEUR}</div></div>
</div>

<h2 class="sec">Spécifications / Specs</h2>
<div class="panel"><table class="vgrid">{VEHICULE}</table></div>

<h2 class="sec">Nomenclature / Bill of items</h2>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article / Part</th><th class="qty">Qté</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">TOTAL <small>— TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<h2 class="sec">Règlement / Payment</h2>
<div class="panel">{PAIEMENT}</div>

<h2 class="sec">Livraison / Delivery</h2>
<div class="panel"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</div>
</body></html>"""

for name, html in [("n_atelier", N), ("o_blueprint", O)]:
    open(f"version_{name}.html", "w").write(html)
    HTML(string=html, base_url=".").write_pdf(f"version_{name}.pdf")
    print(name, "ok")
