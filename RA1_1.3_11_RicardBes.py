# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana un nombre enter de minuts i converteix-lo en hores completes i minuts restants. Utilitza // i %.
# Especificacions d'Entrada: Convertir minuts

minuts = int(input("Introdueix un numero per als minuts:"))

hores = minuts // 60

minuts_sobrants = minuts % 60

print(f"Aquest es el resultat:{hores} hores i {minuts_sobrants} minuts")