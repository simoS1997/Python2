numero = int(input("Introdueixi un número: "))

# Convertim el número a una cadena per poder iterar per cada dígit
cadena_numero = str(numero)

# Iterem per cada dígit de la cadena
for digit in cadena_numero:
    # Convertim el dígit a enter per poder operar amb ell
    digit_enter = int(digit)
    # Comprovem si el dígit és parell
    if digit_enter % 2 == 0:
        print(digit_enter, end=" ")