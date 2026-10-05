# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana tres notes, que poden tenir decimals, i mostra’n la mitjana.
# Especificacions d'Entrada: Mitjana de tres notes

num1 = int(input("Introdueix un numero: "))
num2 = int(input("Introdueix un numero: "))
num3 = int(input("Introdueix un numero: "))

mitjana = num1 + num2 + num3 / 3

print(f"Aquesta es la mitjana de aquests numeros: {mitjana}")