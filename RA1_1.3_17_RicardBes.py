# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana una frase, una paraula que hi aparegui i una paraula nova. Substitueix totes les aparicions de la primera paraula per la segona. Frase: El gat dorm i el gat juga. Paraula a substituir: gat · Paraula nova: gos Resultat: El gos dorm i el gos juga.
# Especificacions d'Entrada: Substituir text

frase = input("Introdueix una frase: ")

paraula_sub = input("Paraula a substituir: ")

paraula_nova = input("Paraula nova: ")

resultat = frase.replace(paraula_sub , paraula_nova)

print("Resultat:", resultat)