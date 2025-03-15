def zad(c):
    n = len(c)
    tab = [0]*n
    tab[0] = c[0]
    tab[1] = max(c[0], c[1])
    for i in range(2,n):
        tab[i] = max(tab[i-1], tab[i-2]+c[i])
    return tab[n-1]