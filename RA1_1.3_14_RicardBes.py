# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana el nom i el cognom, cadascun format per una sola paraula sense accents. Construeix un correu en minúscules amb el format nom.cognom@alumnes.cat.
# Especificacions d'Entrada: Crear un correu electrònic

nom = input("Introdueix el teu nom: ")

cognom = input("Introdueix el teu cognom: ")

print(f"{nom}.{cognom}@institut.cat")