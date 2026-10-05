# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana el radi d’un cercle. Defineix PI = 3.1416 i calcula’n l’àrea. Fórmula: àrea = PI × radi × radi. Mostra el resultat i explica per què escrivim PI en majúscules.
# Especificacions d'Entrada: Quadrat i àrea d’un cercle

PI = 3.1416

num_radi = float(input("Introdueix un numero per al radi del cercle:"))

area = PI * num_radi**2

print(f"L'area del teu cercle es", area)