# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana dos nombres decimals. Mostra amb etiquetes la suma, la resta del primer menys el segon, la multiplicació i la divisió del primer entre el segon. Pots donar per fet que el segon nombre no és zero.
# Especificacions d'Entrada: Calculadora bàsica

print("Posa un numero decimal:")

num1 = float(input())

print("Posa un numero decimal:")

num2 = float(input())

resultat = num1 + num2

print(f"Aquesta es la suma dels numeros introdiuits:{resultat}")



print("Posa un numero decimal:")

num1 = float(input())

print("Posa un numero decimal:")

num2 = float(input())

resultat = num1 - num2

print(f"Aquesta es la resta dels numeros introdiuits:{resultat}")



print("Posa un numero:")

num1 = int(input())

print("Posa un numero:")

num2 = int(input())

resultat = num1 * num2

print(f"Aquesta es la multiplicació dels numeros introdiuits:{resultat}")



print("Posa un numero decimal:")

num1 = float(input())

print("Posa un numero decimal:")

num2 = float(input())

resultat = num1 / num2

print(f"Aquesta es la divisió dels numeros introdiuits:{resultat}")