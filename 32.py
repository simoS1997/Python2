def any(a):
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
        print("Es año bisiesto")
    else:
        print("No es año bisiesto")

#PP
b = input("Indique un año con 4 cifras (aaaa): ")
any(int(b))