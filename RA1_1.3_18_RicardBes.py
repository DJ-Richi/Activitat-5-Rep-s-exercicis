# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana una frase i mostra la frase original, la frase en majúscules, la frase en minúscules i el nombre de caràcters, incloent-hi els espais. Exemple: Hola món té 8 caràcters.
# Especificacions d'Entrada: Majúscules minúscules i longitud

frase = input("Introdueix una frase:")

print("La frase original:", frase)
print("La frase en majúscules:", frase.upper())
print("La frase en minúscules:", frase.lower())
print("Nombre de caracters:", len(frase))