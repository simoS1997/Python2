def esta_ordenada(llista):
    if all(llista[i] <= llista[i+1] for i in range(len(llista)-1)):
        return "ascendent"
    elif all(llista[i] >= llista[i+1] for i in range(len(llista)-1)):
        return "descendent"
    else:
        return "no està ordenada"

#PP
input_str = input("Posa una llista de nombres separats per espais: ")
lst = [int(n) for n in input_str.split()]
orden = esta_ordenada(lst)
print(f"La llista {lst} està ordenada de forma {orden}")
