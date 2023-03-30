num = int(input("Introdueixi un número natural entre 1 i 20: "))
while num < 1 or num > 20:
    num = int(input("Introdueixi un número natural entre 1 i 20: "))

print("Taula de multiplicar del", num)
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
