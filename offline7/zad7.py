from zad7testy import runtests
# Piotr Sękulski
# nr indeksu 422337
# złożoność czasowa O(n) = n^2
# algorytm działa na zasadzie funkcji f(x,y) = maksymalna droga na dane pole w lebiryncie
# algorytm przechodzi każdą kolumne dwa razy najpierw sprawdza wszystkie możliwośći z ruchem w dół a następnie
# przechodzi lebirynt od dołu uwazględniając wcześniej zapisane przejście w dół.


def maze( L ):
    def go_down(n, c, res, arr):
        if arr[0][c] == '.' and res[0][c-1] >= 0:
            res[0][c] = res[0][c-1] + 1
        for i in range(1, n):
            val = max(res[i-1][c], res[i][c-1])
            if arr[i][c] == '.':
                if val > 0:
                    res[i][c] = val + 1

    def go_up(n, c, res, arr):
        par = (-1, -1)  # (j, val on res[j][c-1])
        cnt = 0
        for i in range(n-1, -1, -1):
            if arr[i][c] == '.':
                if par[1] + cnt < res[i][c-1] and res[i][c-1] > 0:
                    par = (i, max(res[i][c-1], 1))
                    cnt = 0
                elif par[1] > 0:
                    cnt += 1
                    res[i][c] = max(res[i][c], par[1] + cnt + 1)
            else:
                par = (-1, -1)
                cnt = 0

    n = len(L)
    res = [[-1 for i in range(n)] for j in range(n)]
    res[0][0] = 0
    for i in range(1,n):
        if L[i][0] == '#':
            break
        res[i][0] = res[i-1][0] + 1
    for i in range(1, n-1):
        go_down(n, i, res, L)
        go_up(n, i, res, L)
    go_down(n, n-1, res, L)
    return res[n-1][n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
