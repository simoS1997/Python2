def eliminarcapicua(llista):
    if llista == []:
        return []
    elif len(llista) == 1:
        return []
    elif llista == llista[::-1]:
        return llista[1:-1]
    else:
        return llista
