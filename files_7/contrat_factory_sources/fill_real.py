#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill template A with real Dos Santos -> Mehidi Clio V E-Tech sale."""
from weasyprint import HTML

src = open('version_a.html').read()

# --- SELLER block ---
seller_old = '''    <p>Raison sociale : <span class="fill f-l"></span></p>
    <p>Adresse : <span class="fill f-xl"></span></p>
    <p>SIREN : <span class="fill f-s"></span> — SIRET : <span class="fill f-m"></span></p>
    <p>Tél. : <span class="fill f-m"></span></p>
    <p>Email : <span class="fill f-l"></span></p>'''
seller_new = '''    <p class="name">DOS SANTOS ALVARELHOS, Kevin</p>
    <p>24 avenue Jean-Jacques Rousseau, 93190 Livry-Gargan</p>
    <p>SIREN : 878 954 130 — RCS Bobigny</p>
    <p>Tél. : +33 7 53 43 30 56</p>
    <p>Négociant automobile (professionnel acquéreur, art. R.322-4 CR)</p>'''
assert seller_old in src
src = src.replace(seller_old, seller_new)

# --- BUYER block ---
buyer_old = '''    <p>Nom, prénom : <span class="fill f-l"></span></p>
    <p>Adresse : <span class="fill f-xl"></span></p>
    <p>Tél. : <span class="fill f-m"></span> &nbsp; Email : <span class="fill f-m"></span></p>
    <p>Pièce d'identité (type et n°) : <span class="fill f-l"></span></p>'''
buyer_new = '''    <p class="name">MÉHIDI Hakim</p>
    <p>Né le 22/07/1995 à Châlons-en-Champagne</p>
    <p>13 rue de Savigny, Escalier 2, 91390 Morsang-sur-Orge</p>
    <p>Tél. : +33 6 52 05 94 22 &nbsp; Email : hakim.mehidi@yahoo.fr</p>'''
assert buyer_old in src
src = src.replace(buyer_old, buyer_new)

# --- doc ref line ---
src = src.replace(
  'N° de contrat : <b>MGP-2026-<span class="fill f-xs"></span></b>',
  'N° de contrat : <b>  </b>')
# in genericized A the ref is different; handle both
src = src.replace(
    'N° de contrat : <b><span class="fill f-s"></span></b>',
    "N° de contrat : <b>GF-405-GG</b>",
)
src = src.replace(
  'Date : <b><span class="fill f-s"></span></b>',
  'Date : <b>02/03/2026</b>')

# --- delivery ---
src = src.replace(
  '<b>Point de livraison</b> <span class="fill f-xl"></span>&nbsp;&nbsp;Date prévue : <span class="fill f-s"></span>',
  '<b>Point de livraison</b> Athis-Mons (91200)&nbsp;&nbsp;Date de remise : 02/03/2026')

# --- vehicle detail (rewrite the whole vgrid rows) ---
veh_old_start = '<table class="vgrid">'
# Replace the entire vgrid content inside item 01 detail
import re
new_vgrid = '''<table class="vgrid">
      <tr><td class="k">Marque, modèle | Puissance</td><td class="v"><b>Renault Clio V E-Tech Hybride — finition Limited</b> | 67 kW (5 CV fisc.)</td></tr>
      <tr><td class="k">VIN | Type-variante-version | Genre</td><td class="v">VF1RJA00168812703 | RJABH2MU4UA3FA5200 | VP</td></tr>
      <tr><td class="k">N° d'immatriculation | Pays</td><td class="v">GF-405-GG | FR</td></tr>
      <tr><td class="k">Carburant | Classe environnementale</td><td class="v">Hybride essence (EH) | Euro 6d</td></tr>
      <tr><td class="k">Kilométrage (non garanti)</td><td class="v">28 500 km</td></tr>
      <tr><td class="k">1<sup>re</sup> mise en circulation | CT valable jusqu'au</td><td class="v">18/03/2022 | 01/10/2027</td></tr>
      <tr><td class="k">Nombre de clés | Propriétaires précédents</td><td class="v"><span class="fill f-xs"></span> | 2</td></tr>
      <tr><td class="k">Accidenté | Véhicule de société</td><td class="v">Non | Non</td></tr>
      <tr><td class="k">Régime de TVA</td><td class="v">TVA sur la marge — art. 297 A CGI</td></tr>
    </table>'''
# find the vgrid block and swap
start = src.find('<table class="vgrid">')
end = src.find('</table>', start) + len('</table>')
src = src[:start] + new_vgrid + src[end:]

# --- items table: fill prices ---
src = src.replace(
  '<tr class="main"><td class="pos">01</td><td><b>Voiture</b></td><td class="qty">01</td><td class="num"><span class="fill f-s"></span> €</td></tr>',
  '<tr class="main"><td class="pos">01</td><td><b>Voiture — Renault Clio V E-Tech Hybride Limited</b></td><td class="qty">01</td><td class="num">15 800,00 €</td></tr>')
src = src.replace(
  '<tr class="discount"><td></td><td>Remise commerciale</td><td class="qty"></td><td class="num">− <span class="fill f-xs"></span> €</td></tr>',
  '<tr class="discount"><td></td><td>Remise commerciale</td><td class="qty"></td><td class="num">— €</td></tr>')
src = src.replace(
  '<tr><td class="pos">02</td><td>Garantie <span class="fill f-xs"></span> mois</td><td class="qty">01</td><td class="num"><span class="fill f-xs"></span> €</td></tr>',
  '<tr><td class="pos">02</td><td>Garantie légale (vices cachés, art. 1641 CC)</td><td class="qty">01</td><td class="num">incluse</td></tr>')
src = src.replace(
  '<tr><td class="pos">03</td><td>Immatriculation (carte grise) par nos soins</td><td class="qty">01</td><td class="num"><span class="fill f-xs"></span> €</td></tr>',
  "<tr><td class=\"pos\">03</td><td>Immatriculation (carte grise) à la charge de l'acheteur</td><td class=\"qty\">01</td><td class=\"num\">— €</td></tr>")
src = src.replace(
  '<tr><td class="pos">04</td><td>Préparation &amp; mise à disposition</td><td class="qty">01</td><td class="num"><span class="fill f-xs"></span> €</td></tr>',
  '<tr><td class="pos">04</td><td>Préparation &amp; mise à disposition</td><td class="qty">01</td><td class="num">incluse</td></tr>')
src = src.replace(
  '<tr><td class="pos">05</td><td>Frais de livraison</td><td class="qty">01</td><td class="num"><span class="fill f-xs"></span> €</td></tr>',
  '<tr><td class="pos">05</td><td>Frais de livraison</td><td class="qty">01</td><td class="num">— €</td></tr>')

# --- total ---
src = src.replace(
  '<div class="t-val"><span class="fill f-s"></span> €</div>',
  '<div class="t-val">15 800,00 €</div>')

# --- payment box ---
src = src.replace(
  '<div><b>Montant du paiement :</b> <span class="fill f-s"></span> €</div>',
  '<div><b>Montant du paiement :</b> 15 800,00 €</div>')
src = src.replace(
  '<p>Titulaire du compte : <span class="fill f-l"></span></p>',
  '<p>Titulaire du compte : DOS SANTOS ALVARELHOS Kevin</p>')
src = src.replace(
  '<p>IBAN : <span class="fill f-xl"></span> &nbsp;&nbsp; BIC : <span class="fill f-s"></span></p>',
  '<p>IBAN : [À COMPLÉTER] &nbsp;&nbsp; BIC : [À COMPLÉTER]</p>')
src = src.replace(
  '<p>Référence à mentionner : <span class="fill f-m"></span></p>',
  '<p>Référence à mentionner : Vente Clio GF-405-GG</p>')

# --- signatures place/date ---
src = src.replace(
  'Fait à <span class="fill f-m"></span>, le <span class="fill f-s"></span>,',
  'Fait à Athis-Mons, le 02/03/2026,')

# --- footer: seller identity ---
src = src.replace(
  'Raison sociale — Forme juridique — Adresse du siège social — SIREN — Capital social (le cas échéant)<br>\n  Tél. — Email — N° TVA intracommunautaire ou mention du régime applicable (à compléter)',
  'DOS SANTOS ALVARELHOS Kevin — SIREN 878 954 130 — RCS Bobigny — 24 avenue Jean-Jacques Rousseau, 93190 Livry-Gargan<br>\n  Tél. +33 7 53 43 30 56 — Régime TVA sur la marge (art. 297 A CGI)')

# --- brand header -> neutral seller banner ---
src = src.replace('<div class="brand">VOTRE <span>ENTREPRISE</span></div>',
                  '<div class="brand">DOS SANTOS <span>AUTOMOBILES</span></div>')
src = src.replace('Logo / activité — Ville', "Négoce de véhicules d'occasion — Livry-Gargan")

open('rempli_dossantos_mehidi.html','w').write(src)
HTML(string=src, base_url='.').write_pdf('rempli_dossantos_mehidi.sour_fill_real_7pdf')
print('filled ok')
