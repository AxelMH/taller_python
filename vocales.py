# Contar vocales en texto.

vocales = ['a', 'e', 'i', 'o', 'u']
texto = str(input("Ingrese texto:"))

# contar por vocales
for vocal in vocales:
    i = 0
    while vocal in texto:
        i += 1
        texto = texto.replace(vocal, '', 1)
    print('hay ' + str(i) + ' ' + vocal + ' en el texto')

"""
# solución 1 (mia) [la peor]
i = 0
for vocal in vocales:
    while vocal in texto:
        i += 1
        texto = texto.replace(vocal, '', 1)

print('hay ' + str(i) + ' vocales en el texto')

# solución 2
i = 0
for letter in texto:
    if letter in vocales:
        i += 1

print('hay ' + str(i) + ' vocales en el texto')
"""

