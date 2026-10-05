# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana el nom, el cognom, l’edat, la ciutat i el cicle formatiu. Genera una fitxa amb el nom complet en majúscules, l’edat que tindrà d’aquí a un any, la ciutat, el cicle i un correu en minúscules amb el format nom.cognom@alumnes.cat. Pots donar per fet que el nom i el cognom són paraules sense espais ni accents. Utilitza + per construir els missatges. FITXA DE L’ALUMNE
# Nom complet: PAU SERRA
# Edat l’any vinent: 19 anys
# Ciutat: Tarragona
# Cicle: ASIX
# Correu: pau.serra@alumnes.cat
# Especificacions d'Entrada: Fitxa de l’alumne

nom = input("Nom: ")
cognom = input("Cognom: ")
edat = int(input("Edat: "))
ciutat = input("Ciutat: ")
cicle = input("Cicle formatiu: ")

correu = nom.lower() + "." + cognom.lower() + "@alumnes.cat"
print("\n")
print("============================")
print("FITXA DE L'ALUMNE")
print("Nom complet: " + nom.upper() + " " + cognom.upper())
print("Edat l'any vinent: " + str(edat + 1) + " anys")
print("Ciutat: " + ciutat)
print("Cicle: " + cicle)
print("Correu: " + correu)
print("============================")