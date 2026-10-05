# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana una frase amb espais al principi i al final. Elimina aquests espais, conservant els espais interiors, i mostra el resultat entre claudàtors. Entrada: "   Aprenem Python   " Resultat: [Aprenem Python]
# Especificacions d'Entrada: Netejar una frase

frase = input("Introdueix una frase: ")

longitud_frase = len(frase)

frase_nova = frase[1:longitud_frase -1]

print([frase_nova])