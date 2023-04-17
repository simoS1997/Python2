# Función para comprobar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Buscamos los números primos entre 1 y 100
primos = []
for i in range(1, 101):
    if es_primo(i):
        primos.append(i)

# Mostramos los números primos encontrados y su cantidad
print("Los números primos entre 1 y 100 son:")
for primo in primos:
    print(primo, end=" ")
print(f"\nHay {len(primos)} números primos en total.")
