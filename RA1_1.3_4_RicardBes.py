# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Aquest programa hauria de mostrar l’edat que tindrà l’usuari d’aquí a cinc anys. Explica l’error i escriu el programa corregit.
# Especificacions d'Entrada: Detectar i corregir un error

# Original / mal
edat = input("Quants anys tens? ")
edat_futura = edat + 5
print(edat_futura)

# Alterat / be
edat = int(input("Quants anys tens? "))
edat_futura = edat + 5
print(edat_futura)