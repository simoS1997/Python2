def esta_ordenada(llista):
    if all(llista[i] <= llista[i+1] for i in range(len(llista)-1)):
        return "ascendent"
    elif all(llista[i] >= llista[i+1] for i in range(len(llista)-1)):
        return "descendent"
    else:
        return "no està ordenada"
