"""ejercicio 2."""
x = float(input('Ingrese el primer número: '))
y = float(input('Ingrese el segundo número: '))

#print('Ingese el número de la operación que desea realizar\n1.- Suma\n2.- Resta\n3.- Multiplicación\n')
opcion=int(input('Ingese el número de la operación que desea realizar\n1.- Suma\n2.- Resta\n3.- Multiplicación\n'))

if opcion>3 or opcion<1:
    print('Opción incorrecta')
elif opcion==1:
    print(x+y)
elif opcion==2:
    print(x-y)
else:
    print(x*y)
   