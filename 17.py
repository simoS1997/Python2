def invertir(a):
    b = list(a)
    c = b[::-1]
    r = "".join(c)
    return r

def es_palindrome(a):
    c = invertir(a)
    x = 0
    for i in range(len(a)):
        if a[i]!=c[1]:
            x+=1
    if x==0:
        return True
    else:
        return False

x = input("Introdueix una ")
