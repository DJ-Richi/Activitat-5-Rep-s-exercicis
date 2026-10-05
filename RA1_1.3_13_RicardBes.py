# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana una paraula i mostra-la quatre vegades seguides sense espais i, en una altra línia, tres vegades separades per espais, sense espai al final. Utilitza * almenys una vegada.
# Especificacions d'Entrada: Repetir una paraula

paraula = input("Introdueix una paraula per a que es repeteixi: ")

cadena = paraula * 4

print(cadena)


paraula = input("Introdueix una paraula per a que es repeteixi: ") + " "

cadena = paraula * 4

print(cadena)
