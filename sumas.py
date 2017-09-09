
array=[]
try:
	array.append(int(input("Ingrese el valor 1: ")))
	array.append(int(input("Ingrese el valor 2: ")))
	array.append(int(input("Ingrese el valor 3: ")))
	array.append(int(input("Ingrese el valor 4: ")))
	array.append(int(input("Ingrese el valor 5: ")))
	print(array[0]+array[1]+array[2]+array[3]+array[4])
except:
	print("error")
