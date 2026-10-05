# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana un nom d’usuari que pot contenir espais al principi i al final i lletres majúscules. Elimina els espais dels extrems, converteix-lo a minúscules i mostra el nom resultant i la seva longitud.
# Especificacions d'Entrada: Preparar un nom d’usuari

usuari = input("Introdueix un nom d'usuari: ")

usuari = usuari.strip().lower()

print("Usuari:", usuari)
print("Caràcters:", len(usuari))