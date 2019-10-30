ranI = int(input("n1 = "))
ranF = int(input("n2 = "))

acumulador = ""

if (ranI<ranF) :
	for i in range(ranI, ranF+1) :
		acumulador = acumulador + str(i) + " "
		
else :
	for i in range(ranI, ranF-1, -1) :
		acumulador = acumulador + str(i) + " "

print("")
print("La serie es: ", acumulador)