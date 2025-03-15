from kol3testy import runtests
# Piotr Sękulski 422337
# złożoność algorytmu O(n^2)
# algorytm działa na zasadzie funkcji podanej z podpowiedzi to jest algorytm w karzdym przejściu pentli
# for z argumętem i przyjmuje ite drzewo póżniej przechodzimy przez tablice dynamiczną w której jty indeks wskazuje
# na modulo m z sumy jabłek na niewyciętych drzewach przyjmując że wycinaliśmy k poprzednich drzew i zapamiętujemy
# w jednej krotce wybieramy ten wynik w którym wycieliśmy mniej drzew. zapamiętujemy to w tablicy dynamicznej stanów.
# algorytm dało by się trochę przyspiezyć wykorzystując słowniki bo w tedy uzyskamy prawdziwą zlożoność O(n^2)
# a aktualnie z braku czasu nie byłem w stanie tego zaimplemętować więc mój algorytm ma tak naprawdę złożoność O(n * m)

def orchard(T, m):
    # tu prosze wpisac wlasna implementacje
    sum = 0
    n = len(T)
    for i in T:
        sum += i
    mod_m = sum % m
    if m > sum: return len(T)
    dp = [[-1 for i in range(m)] for j in range(n)]
    dp[0][mod_m] = (sum, 0)
    if (sum - T[0]) % m != mod_m:
        dp[0][(sum - T[0]) % m] = (sum - T[0], 1)
    for i in range(1, n):
        for j in range(1, m):
            if dp[i - 1][j] != -1:
                sum, cut = dp[i - 1][j]
                if dp[i][(sum - T[i]) % m] == -1:
                    dp[i][(sum - T[i]) % m] = (sum - T[i], cut + 1)
                else:
                    if cut + 1 < dp[i][(sum - T[i]) % m][1]:
                        dp[i][(sum - T[i]) % m] = (sum - T[i], cut + 1)
                if dp[i][j] == -1:
                    dp[i][j] = (sum, cut)
                else:
                    if cut < dp[i][j][1]:
                        dp[i][j] = (sum, cut)
    min_to_cut = float("inf")
    for i in range(n):
        if dp[i][0] != -1:
            min_to_cut = min(min_to_cut, dp[i][0][1])

    return min_to_cut


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
