
"""
list = [1, 2, 3, 4, 5, 6]
for element in list:
    print(element)

list2 = [1, 2, 'hola', 4, 5, 6]
for element in list2:
    print(element)

range = range(0, 60)
for element in range:
    print(element)

#mostrar elemntos de la matriz
matrix = [['pollo', 3, 1.5], ['queso', 2, 3.8], ['queso', 2, 'uno', 1.1]]
for row in matrix:
    for element in row:
            print(element)

# mostrar elementos de la matriz que sean string
matrix = [['pollo', 3, 1.5], ['queso', 2, 3.8], ['jamón', 2, 'uno', 1.1]]
for row in matrix:
    for element in row:
        if isinstance(element, str):
            print(element)
"""

#menor = int(input('Ingresar un número: '))
#mayor = int(input('Ingresar un número mayor que el anterior: '))
nums = []
nums.append(int(input('Ingresar un número: ')))
nums.append(int(input('Ingresar un número: ')))

mayor = max(nums)
menor = min(nums)

i = 0

while menor < mayor:
    i += 1
    menor += 1
    if menor == mayor:
        break
    mayor -= 1
    if menor == mayor:
        break

print('Se iteró ' + str(i) + ' veces para llegar al número ' + str(menor))
