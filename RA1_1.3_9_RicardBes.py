# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana el preu d’un producte sense IVA i el nombre d’unitats. Calcula i mostra l’import de la compra sense IVA, l’import de l’IVA del 21 % i el total amb IVA.
# Especificacions d'Entrada: Compra amb IVA

IVA = 0.21

num_preu = float(input("Introdueix un numero:"))

unitats = int(input("Introdueix un numero d'unitats"))

preu = (num_preu * IVA + num_preu)

unitats_amb_preu = (preu * unitats)

print(f"El teu producte amb IVA es: {preu} i amb les unitats introduïdes es: {unitats_amb_preu}")