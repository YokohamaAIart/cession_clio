#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Template M — Día de los Muertos."""
import urllib.parse
import gen_fun as gf
from weasyprint import HTML

VENDEUR, ACHETEUR, VEHICULE, ITEMS = gf.VENDEUR, gf.ACHETEUR, gf.VEHICULE, gf.ITEMS
PAIEMENT, LIVRAISON, SIGNATURES, FOOTER = gf.PAIEMENT, gf.LIVRAISON, gf.SIGNATURES, gf.FOOTER
BASE, FILLS = gf.BASE, gf.FILLS

# --- sugar skull SVG watermark (soft violet, behind content) ---
skull = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 240">
<g fill="none" stroke="#7b2ff7" stroke-width="3">
<path d="M100 12 C48 12 26 50 26 96 C26 132 40 152 52 162 L52 196 C52 210 62 218 74 218 L126 218 C138 218 148 210 148 196 L148 162 C160 152 174 132 174 96 C174 50 152 12 100 12 Z"/>
<circle cx="66" cy="96" r="24"/><circle cx="134" cy="96" r="24"/>
<circle cx="66" cy="96" r="12" stroke-dasharray="4 5"/><circle cx="134" cy="96" r="12" stroke-dasharray="4 5"/>
<path d="M100 122 L88 144 L112 144 Z"/>
<path d="M70 176 L130 176 M80 166 L80 186 M92 164 L92 190 M104 164 L104 190 M116 166 L116 186"/>
<path d="M100 34 L100 52 M91 43 L109 43" />
<circle cx="42" cy="140" r="7"/><circle cx="158" cy="140" r="7"/>
<path d="M60 58 C66 48 78 48 82 56 M118 56 C122 48 134 48 140 58"/>
</g></svg>"""
skull_uri = "data:image/svg+xml," + urllib.parse.quote(skull)

M = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:8mm 12mm 7mm 12mm; }}
{BASE}{FILLS}
:root {{ --noche:#241436; --cempa:#f2790f; --rosa:#e91e8c; --turq:#00a99b; --viol:#7b2ff7; --paper:#fdf8ef; --line:#ecd9c8; --muted:#9a8a90; }}
body {{ font-size:9.4px; font-family:"Liberation Sans",sans-serif; color:#33222e; background:var(--paper); }}
h1,h2,h4 {{ font-family:"Lora",serif; }}
.fill {{ border-bottom:1px dotted #c7ab9e; }}
.skullwm {{ position:fixed; top:96mm; left:58mm; width:94mm; height:113mm; z-index:-1; opacity:0.09;
  background-image:url('{skull_uri}'); background-size:100% 100%; }}
.picado {{ height:8px; background:repeating-linear-gradient(90deg,var(--rosa) 0px,var(--rosa) 24px,var(--cempa) 24px,var(--cempa) 48px,var(--turq) 48px,var(--turq) 72px,var(--viol) 72px,var(--viol) 96px); border-radius:2px; }}
.picado.bottom {{ margin-top:5px; }}
.hero {{ background:var(--noche); border-radius:0 0 14px 14px; color:#fff; text-align:center; padding:10px 16px 9px 16px; }}
.hero .orn {{ color:var(--cempa); font-size:9.5px; letter-spacing:7px; }}
.hero h1 {{ font-size:19px; font-weight:700; font-style:italic; color:#fff; margin:2px 0 0 0; }}
.hero h1 .r {{ color:var(--rosa); }} .hero h1 .o {{ color:var(--cempa); }} .hero h1 .t {{ color:var(--turq); }}
.hero .sub {{ font-size:8.2px; letter-spacing:3.5px; text-transform:uppercase; color:#d9b8ff; margin-top:2px; }}
.hero .ref {{ font-size:8.6px; color:#cfc0dd; margin-top:4px; }}
.hero .fill {{ border-bottom-color:#8d7aa8; }}
.course {{ margin:8px 0 3.5px 0; }}
.course h2 {{ display:inline; font-size:11.5px; font-style:italic; font-weight:700; color:var(--noche); }}
.course h2::before {{ content:"✿ "; color:var(--cempa); font-style:normal; }}
.course .es {{ font-size:8px; font-style:italic; color:var(--rosa); margin-left:7px; }}
.panel {{ background:rgba(255,253,248,0.72); border:1px solid var(--line); border-radius:10px; padding:7px 12px; }}
.panel.b-rosa {{ border-top:2.5px solid var(--rosa); }}
.panel.b-turq {{ border-top:2.5px solid var(--turq); }}
.panel.b-cempa {{ border-top:2.5px solid var(--cempa); }}
.panel.b-viol {{ border-top:2.5px solid var(--viol); }}
.panel p {{ margin-bottom:2.6px; }}
.vgrid .k {{ color:var(--muted); }}
.vgrid .v b {{ color:var(--rosa); }}
table.items th {{ font-family:"Lora"; font-style:italic; font-weight:700; font-size:9px; color:#fff; background:var(--noche); text-align:left; padding:4.5px 10px; }}
table.items th:first-child {{ border-radius:10px 0 0 0; }} table.items th:last-child {{ border-radius:0 10px 0 0; }}
table.items td {{ padding:4.2px 10px; border-bottom:1px dotted var(--line); background:rgba(255,253,248,0.72); }}
table.items td.pos {{ color:var(--cempa); font-weight:bold; }}
tr.discount td {{ color:var(--turq); font-style:italic; }}
tr.total {{ background:linear-gradient(90deg,var(--rosa),var(--cempa)); }}
tr.total td {{ background:transparent; color:#fff; font-family:"Lora"; font-style:italic; font-weight:700; font-size:11.5px; padding:6px 10px; border-bottom:none; }}
tr.total td:first-child {{ border-radius:0 0 0 10px; }} tr.total td:last-child {{ border-radius:0 0 10px 0; font-size:13px; }}
tr.total td small {{ font-family:"Liberation Sans"; font-style:normal; font-weight:normal; font-size:7.6px; }}
tr.total .fill {{ border-bottom-color:#ffd9ec; }}
.sig {{ border:1.5px dashed var(--rosa); border-radius:10px; background:rgba(255,253,248,0.8); }}
.sig h4 {{ font-style:italic; font-weight:700; font-size:10px; color:var(--noche); }}
.sig h4::before {{ content:"✦ "; color:var(--turq); font-style:normal; }}
.sig p {{ font-size:7.8px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:8px 2px 5px 2px; text-align:center; font-style:italic; font-family:"Lora"; }}
.flor {{ text-align:center; color:var(--cempa); font-size:9px; letter-spacing:8px; margin-top:4px; }}
.footer {{ margin-top:5px; text-align:center; font-size:7.2px; color:var(--muted); line-height:1.6; border-top:1px solid var(--line); padding-top:4px; }}
</style></head><body>

<div class="skullwm"></div>
<div class="picado"></div>
<div class="hero">
  <div class="orn">✿ ❀ ✿ ❀ ✿</div>
  <h1>Contrato de Venta — <span class="r">Día</span> <span class="o">de los</span> <span class="t">Muertos</span></h1>
  <div class="sub">Contrat de vente — Véhicule d'occasion — La Clio ne meurt jamais, elle change de mains</div>
  <div class="ref">N° de contrat : <span class="fill f-s"></span> &nbsp;•&nbsp; Date : <span class="fill f-s"></span></div>
</div>

<div class="row" style="margin-top:7px">
  <div class="half"><div class="course"><h2>Vendeur</h2><span class="es">el que la deja partir</span></div><div class="panel b-rosa">{VENDEUR}</div></div>
  <div class="half"><div class="course"><h2>Acheteur</h2><span class="es">el que la recibe</span></div><div class="panel b-turq">{ACHETEUR}</div></div>
</div>

<div class="course"><h2>Le véhicule</h2><span class="es">la calavera mecánica — Renault Clio</span></div>
<div class="panel b-cempa"><table class="vgrid">{VEHICULE}</table></div>

<div class="course"><h2>Produits et services</h2><span class="es">la ofrenda</span></div>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">Total <small>— TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<div class="course"><h2>Paiement</h2><span class="es">el tributo, antes de la procesión</span></div>
<div class="panel b-viol">{PAIEMENT}</div>

<div class="course"><h2>Livraison</h2><span class="es">la procesión final</span></div>
<div class="panel b-rosa"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="flor">✿ ❀ ✿</div>
<div class="footer">{FOOTER}</div>
<div class="picado bottom"></div>
</body></html>"""

open("version_m_muertos.html", "w").write(M)
HTML(string=M, base_url=".").write_pdf("version_m_muertos.pdf")
print("m ok")
