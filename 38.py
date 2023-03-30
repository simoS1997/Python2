num = int(input("Introdueix un número entre 1 i 900000: "))

if num < 1 or num > 900000:
    print("El número introduït no és vàlid.")
else:
    digits = len(str(num))
    print("El número {} té {} dígits.".format(num, digits))