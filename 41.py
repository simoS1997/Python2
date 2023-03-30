num = input("Introdueix un número: ")
suma = 0
for digit in num:
    suma += int(digit)
    
if suma % 2 == 0:
    print("La suma dels dígits és parell.")
else:
    print("La suma dels dígits és senar.")