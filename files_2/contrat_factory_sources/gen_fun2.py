#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Templates G (Geek LLM), H (Art déco), I (Japon) — reuse fragments from gen_fun."""
import gen_fun as gf  # renders A-F side effect, cheap
from weasyprint import HTML

VENDEUR, ACHETEUR, VEHICULE, ITEMS = gf.VENDEUR, gf.ACHETEUR, gf.VEHICULE, gf.ITEMS
PAIEMENT, LIVRAISON, SIGNATURES, FOOTER = gf.PAIEMENT, gf.LIVRAISON, gf.SIGNATURES, gf.FOOTER
BASE, FILLS = gf.BASE, gf.FILLS

# ================================================================ TEMPLATE G
# Geek LLM — code-editor light theme, YAML/prompt aesthetics
G = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:9mm 11mm 8mm 11mm; }}
{BASE}{FILLS}
:root {{ --bg:#fbfbfd; --panel:#f6f8fa; --line:#d0d7de; --ink:#1f2328; --blue:#0969da; --purple:#8250df; --green:#1a7f37; --red:#cf222e; --gray:#656d76; }}
body {{ font-family:"DejaVu Sans Mono",monospace; font-size:8.8px; color:var(--ink); background:var(--bg); }}
.fill {{ border-bottom:1px dotted #adb5bd; }}
.window {{ border:1px solid var(--line); border-radius:8px; overflow:hidden; background:#fff; }}
.titlebar {{ background:#eceff2; border-bottom:1px solid var(--line); padding:5px 10px; display:flex; align-items:center; gap:6px; }}
.dot {{ width:8px; height:8px; border-radius:50%; }}
.d1 {{ background:#ff5f57; }} .d2 {{ background:#febc2e; }} .d3 {{ background:#28c840; }}
.titlebar .path {{ margin-left:8px; color:var(--gray); font-size:8.2px; }}
.winbody {{ padding:9px 12px; }}
.prompt {{ color:var(--gray); }}
.prompt b {{ color:var(--ink); font-weight:normal; }}
.k {{ color:var(--purple); }} .str {{ color:var(--blue); }} .cm {{ color:var(--green); }} .fn {{ color:var(--red); }}
h1.cmd {{ font-size:13px; font-weight:bold; color:var(--ink); }}
h1.cmd .fn {{ font-weight:bold; }}
.meta {{ display:flex; gap:8px; margin:6px 0 0 0; flex-wrap:wrap; }}
.tag {{ background:var(--panel); border:1px solid var(--line); border-radius:99px; padding:1px 9px; font-size:7.6px; color:var(--gray); }}
.tag b {{ color:var(--green); font-weight:normal; }}
h2.sec {{ font-size:9px; color:var(--green); margin:9px 0 3px 0; font-weight:normal; }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:6px; padding:7px 11px; }}
.panel p {{ margin-bottom:2.6px; }}
.vgrid .k2 {{ color:var(--purple); }}
.vgrid td.k {{ color:var(--purple); width:44%; padding-right:8px; }}
.vgrid .v b {{ color:var(--blue); }}
table.items {{ border:1px solid var(--line); border-radius:6px; }}
table.items th {{ font-size:8px; color:var(--gray); background:var(--panel); text-align:left; padding:4px 9px; border-bottom:1px solid var(--line); }}
table.items td {{ padding:4px 9px; border-bottom:1px solid #e8ebee; background:#fff; }}
table.items td.pos {{ color:var(--gray); }}
tr.discount td {{ color:var(--red); }}
tr.total td {{ background:var(--panel); border-top:1px solid var(--line); border-bottom:none; font-weight:bold; font-size:10.5px; padding:6px 9px; }}
tr.total td:last-child {{ color:var(--green); font-size:12px; }}
tr.total td small {{ font-weight:normal; font-size:7.2px; color:var(--gray); }}
.sig {{ border:1px dashed var(--line); border-radius:6px; background:#fff; }}
.sig h4 {{ font-size:8.8px; color:var(--purple); }}
.sig h4::before {{ content:">>> "; color:var(--gray); }}
.sig p {{ font-size:7.6px; color:var(--gray); margin-top:2px; }}
.sig-intro {{ margin:9px 1px 5px 1px; color:var(--gray); }}
.footer {{ margin-top:8px; text-align:center; font-size:6.8px; color:var(--gray); line-height:1.7; }}
.footer::before {{ content:"<EOS> "; color:var(--red); }}
</style></head><body>

<div class="window">
  <div class="titlebar"><span class="dot d1"></span><span class="dot d2"></span><span class="dot d3"></span><span class="path">~/contrats/vente_clio_v1.yaml — édité par un humain, relu par un LLM</span></div>
  <div class="winbody">
    <h1 class="cmd"><span class="fn">contrat_de_vente</span>(<span class="str">"vehicule_occasion"</span>, model=<span class="str">"renault_clio"</span>)</h1>
    <div class="prompt"># <span class="cm">system: tu es un contrat. Sois clair, complet, et tiens sur une page.</span></div>
    <div class="meta">
      <span class="tag">n°_contrat: <span class="fill f-s"></span></span>
      <span class="tag">date: <span class="fill f-s"></span></span>
      <span class="tag">temperature: <b>0.0</b> — zéro hallucination</span>
      <span class="tag">context_window: <b>1 page</b></span>
      <span class="tag">signatures_requises: <b>2</b></span>
    </div>
  </div>
</div>

<div class="row" style="margin-top:8px">
  <div class="half"><h2 class="sec"># --- vendeur: (humain, rôle: assistant commercial) ---</h2><div class="panel">{VENDEUR}</div></div>
  <div class="half"><h2 class="sec"># --- acheteur: (humain, rôle: user) ---</h2><div class="panel">{ACHETEUR}</div></div>
</div>

<h2 class="sec"># --- vehicule: (payload principal, non compressé) ---</h2>
<div class="panel"><table class="vgrid">{VEHICULE}</table></div>

<h2 class="sec"># --- items: sum() → total, aucune inférence sur les prix ---</h2>
<table class="items">
  <tr><th style="width:22px">#</th><th>article</th><th class="qty">nombre</th><th class="num" style="width:90px">prix_€</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">total <small># TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<h2 class="sec"># --- paiement: virement_bancaire(pre_livraison=True) ---</h2>
<div class="panel">{PAIEMENT}</div>

<h2 class="sec"># --- livraison: await handover() ---</h2>
<div class="panel"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</body></html>"""

# ================================================================ TEMPLATE H
# Art déco — black & gold Gatsby, geometric frames
H = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:8mm 10mm 7mm 10mm; }}
{BASE}{FILLS}
:root {{ --black:#151412; --gold:#c9a227; --gold2:#e6cf7a; --cream:#faf6ec; --line:#d8c98f; --muted:#8b8471; }}
body {{ font-family:"Liberation Sans",sans-serif; font-size:9.4px; color:#2b2820; background:var(--cream); }}
h1,h2,h4 {{ font-family:"Lora",serif; }}
.fill {{ border-bottom:1px dotted #b3a878; }}
.frame {{ border:2px solid var(--gold); outline:1px solid var(--gold); outline-offset:3px; padding:7mm 8mm 5mm 8mm; }}
.hero {{ text-align:center; border-bottom:1.5px solid var(--gold); padding-bottom:7px; }}
.orn {{ color:var(--gold); font-size:10px; letter-spacing:8px; }}
.hero h1 {{ font-size:19px; font-weight:700; letter-spacing:4px; text-transform:uppercase; color:var(--black); margin:3px 0 1px 0; }}
.hero .sub {{ font-size:8.4px; letter-spacing:5px; text-transform:uppercase; color:var(--gold); }}
.hero .ref {{ font-size:8.8px; margin-top:5px; color:var(--muted); }}
.deco-sec {{ text-align:center; margin:9px 0 4px 0; }}
.deco-sec h2 {{ display:inline-block; font-size:11px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:var(--black); border-bottom:1.5px solid var(--gold); padding:0 14px 2px 14px; }}
.deco-sec .side {{ color:var(--gold); font-size:9px; vertical-align:2px; letter-spacing:0; }}
.panel {{ border:1px solid var(--line); background:#fffdf6; padding:7px 12px; }}
.panel p {{ margin-bottom:2.6px; }}
.vgrid .k {{ color:var(--muted); }}
.vgrid .v b {{ color:var(--black); }}
table.items {{ border:1px solid var(--gold); }}
table.items th {{ font-family:"Lora"; font-weight:700; font-size:8.8px; letter-spacing:2px; text-transform:uppercase; color:var(--gold2); background:var(--black); text-align:left; padding:5px 10px; }}
table.items td {{ padding:4.2px 10px; border-bottom:1px solid #ecdfae; background:#fffdf6; }}
table.items td.pos {{ color:var(--gold); font-family:"Lora"; font-weight:700; }}
tr.discount td {{ color:var(--muted); font-style:italic; }}
tr.total td {{ background:var(--black); color:var(--gold2); font-family:"Lora"; font-weight:700; font-size:11.5px; letter-spacing:1px; padding:6.5px 10px; border-bottom:none; }}
tr.total td:last-child {{ font-size:13.5px; }}
tr.total td small {{ font-family:"Liberation Sans"; font-weight:normal; font-size:7.4px; letter-spacing:0; color:#cbbd85; }}
tr.total .fill {{ border-bottom-color:#8c7c3e; }}
.sig {{ border:1.5px solid var(--gold); background:#fffdf6; position:relative; }}
.sig h4 {{ font-weight:700; font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--black); }}
.sig h4::before {{ content:"◆ "; color:var(--gold); font-size:7.6px; }}
.sig p {{ font-size:7.8px; color:var(--muted); margin-top:2px; }}
.sig-intro {{ margin:9px 2px 5px 2px; }}
.footer {{ margin-top:8px; text-align:center; font-size:7.2px; color:var(--muted); line-height:1.6; border-top:1px solid var(--line); padding-top:5px; }}
.gap {{ height:8px; }}
</style></head><body>
<div class="frame">

<div class="hero">
  <div class="orn">◆ ◇ ◆ ◇ ◆</div>
  <h1>Contrat de Vente</h1>
  <div class="sub">Véhicule d'occasion — Grande Élégance Automobile</div>
  <div class="ref">N° de contrat : <span class="fill f-s"></span> &nbsp;•&nbsp; Date : <span class="fill f-s"></span></div>
</div>

<div class="row" style="margin-top:8px">
  <div class="half"><div class="deco-sec"><span class="side">◆—</span><h2>Vendeur</h2><span class="side">—◆</span></div><div class="panel">{VENDEUR}</div></div>
  <div class="half"><div class="deco-sec"><span class="side">◆—</span><h2>Acheteur</h2><span class="side">—◆</span></div><div class="panel">{ACHETEUR}</div></div>
</div>

<div class="deco-sec"><span class="side">◆—</span><h2>L'Automobile</h2><span class="side">—◆</span></div>
<div class="panel"><table class="vgrid">{VEHICULE}</table></div>

<div class="gap"></div>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">Total <small>— TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<div class="deco-sec"><span class="side">◆—</span><h2>Paiement</h2><span class="side">—◆</span></div>
<div class="panel">{PAIEMENT}</div>

<div class="deco-sec"><span class="side">◆—</span><h2>Livraison</h2><span class="side">—◆</span></div>
<div class="panel"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>

</div>
</body></html>"""

# ================================================================ TEMPLATE I
# Japon — washi, sumi ink, vermillon hanko seal
I = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:9mm 12mm 8mm 12mm; }}
{BASE}{FILLS}
:root {{ --sumi:#2b2b2b; --verm:#c73e3a; --washi:#fbf8f1; --line:#e4ddcd; --muted:#8f887a; }}
body {{ font-family:"Liberation Sans",sans-serif; font-size:9.5px; color:var(--sumi); background:var(--washi); }}
h1,h2,h4 {{ font-family:"Lora",serif; }}
.jp {{ font-family:"TakaoPGothic","Noto Sans CJK JP","DejaVu Sans",sans-serif; }}
.fill {{ border-bottom:1px dotted #b8ae97; }}
.hero {{ display:flex; justify-content:space-between; align-items:flex-start; border-bottom:2.5px solid var(--sumi); padding-bottom:8px; }}
.hero .l {{ border-left:4px solid var(--verm); padding-left:12px; }}
.hero h1 {{ font-size:17px; font-weight:700; letter-spacing:1px; }}
.hero .sub {{ font-size:8.6px; letter-spacing:3.5px; text-transform:uppercase; color:var(--verm); margin-top:2px; }}
.hero .ref {{ font-size:8.8px; color:var(--muted); margin-top:4px; }}
.hanko {{ width:60px; height:60px; border-radius:50%; border:2.5px solid var(--verm); color:var(--verm); text-align:center; font-size:20px; line-height:56px; font-weight:bold; flex-shrink:0; transform:rotate(6deg); background:#fff6f4; }}
h2.sec {{ font-size:10.5px; font-weight:700; margin:10px 0 4px 0; }}
h2.sec::before {{ content:"— "; color:var(--verm); }}
h2.sec .jpx {{ font-size:8.4px; color:var(--muted); font-weight:normal; margin-left:6px; }}
.panel {{ background:#fffdf8; border:1px solid var(--line); border-left:3px solid var(--sumi); padding:7px 12px; }}
.panel.red {{ border-left-color:var(--verm); }}
.panel p {{ margin-bottom:2.6px; }}
.vgrid .k {{ color:var(--muted); }}
.vgrid .v b {{ color:var(--verm); }}
table.items th {{ font-family:"Lora"; font-weight:700; font-size:8.8px; letter-spacing:1px; color:#fff; background:var(--sumi); text-align:left; padding:4.5px 10px; }}
table.items td {{ padding:4.2px 10px; border-bottom:1px solid var(--line); background:#fffdf8; }}
table.items td.pos {{ color:var(--verm); }}
tr.discount td {{ color:var(--muted); font-style:italic; }}
tr.total td {{ background:var(--verm); color:#fff; font-family:"Lora"; font-weight:700; font-size:11px; padding:6px 10px; border-bottom:none; }}
tr.total td:last-child {{ font-size:13px; }}
tr.total td small {{ font-family:"Liberation Sans"; font-weight:normal; font-size:7.6px; }}
tr.total .fill {{ border-bottom-color:#f0c3c1; }}
.sig {{ border:1px solid var(--sumi); background:#fffdf8; position:relative; }}
.sig h4 {{ font-weight:700; font-size:9.8px; }}
.sig p {{ font-size:7.8px; color:var(--muted); margin-top:2px; }}
.sig .mini {{ position:absolute; right:9px; top:8px; width:26px; height:26px; border-radius:50%; border:1.5px solid var(--verm); color:var(--verm); text-align:center; font-size:9px; line-height:23px; transform:rotate(8deg); }}
.sig-intro {{ margin:10px 2px 5px 2px; }}
.footer {{ margin-top:9px; text-align:center; font-size:7.4px; color:var(--muted); line-height:1.6; border-top:1px solid var(--line); padding-top:5px; }}
.gap {{ height:8px; }}
</style></head><body>

<div class="hero">
  <div class="l">
    <h1>Contrat de Vente — Véhicule d'Occasion</h1>
    <div class="sub">Édition Yokohama — sobriété, précision, harmonie</div>
    <div class="ref">N° de contrat : <span class="fill f-s"></span> &nbsp;•&nbsp; Date : <span class="fill f-s"></span></div>
  </div>
  <div class="hanko jp">契約</div>
</div>

<div class="row" style="margin-top:6px">
  <div class="half"><h2 class="sec">Vendeur <span class="jpx jp">売主</span></h2><div class="panel">{VENDEUR}</div></div>
  <div class="half"><h2 class="sec">Acheteur <span class="jpx jp">買主</span></h2><div class="panel">{ACHETEUR}</div></div>
</div>

<h2 class="sec">Le véhicule <span class="jpx jp">車両 — Renault Clio</span></h2>
<div class="panel red"><table class="vgrid">{VEHICULE}</table></div>

<h2 class="sec">Produits et services <span class="jpx jp">明細</span></h2>
<table class="items">
  <tr><th style="width:22px">#</th><th>Article</th><th class="qty">Nombre</th><th class="num" style="width:90px">Prix €</th></tr>
  {ITEMS}
  <tr class="total"><td colspan="3">Total <small>— TVA incluse (selon régime applicable)</small></td><td class="num"><span class="fill f-s"></span> €</td></tr>
</table>

<h2 class="sec">Paiement <span class="jpx jp">支払い</span></h2>
<div class="panel">{PAIEMENT}</div>

<h2 class="sec">Livraison <span class="jpx jp">納車</span></h2>
<div class="panel"><p>{LIVRAISON}</p></div>

{SIGNATURES}
<div class="footer">{FOOTER}</div>
</body></html>"""

for name, html in [("g_geek_llm", G), ("h_artdeco", H), ("i_japon", I)]:
    open(f"version_{name}.html", "w").write(html)
    HTML(string=html, base_url=".").write_pdf(f"version_{name}.pdf")
    print(name, "ok")
