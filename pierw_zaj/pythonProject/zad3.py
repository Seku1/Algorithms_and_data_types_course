def zad3(tab):
    n = len(tab)
    m = tab(n-1)
    if m == n - 1:
        return m + 1
    pocz, kon = 0, n-1
    while pocz != kon:
        sr = (pocz + kon) // 2
        if tab[sr] == sr:
            pocz = sr
        else:
            kon = sr
