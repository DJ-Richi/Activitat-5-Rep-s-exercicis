# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/10/2026
# Versió: 1
#
# Descripció: Demana una temperatura en graus Celsius i mostra l’equivalent en Fahrenheit. Fórmula: F = C × 9 / 5 + 32.
# Especificacions d'Entrada: Conversió de temperatura

temp = float(input("Introdueix un numero de temperatura: "))

farenheit = (temp * 1.8) + 32

print(f"{temp} °C equivalen a {farenheit} °F")