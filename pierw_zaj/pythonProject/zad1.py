def zad1(tab):
    i = 1
    max = tab[0]
    min = tab[0]
    while i < len(tab):
        if tab[i] < tab[i + 1]:
            tab[i], tab[i + 1] = tab[i + 1], tab[i]
        if tab[i] > max:
            max = tab[i]
        if tab[i+1] < min:
            min = tab[i+1]
        if i +1 != tab[len(tab) - 1]:
            max = tab[len(tab) - 1]
        elif min == tab[len(tab) - 1]:
            min = tab[len(tab) - 1]
        return (min, max)
