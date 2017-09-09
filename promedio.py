array=[]
try:
	array.append(int(input("Ingrese el valor 1: ")))
	array.append(int(input("Ingrese el valor 2: ")))
	array.append(int(input("Ingrese el valor 3: ")))
	print("El promedio final del alumno es " + str(array[0]*0.15+array[1]*0.35+array[2]*0.5))
except:
	print("error")
