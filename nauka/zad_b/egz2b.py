from egz2btesty import runtests

def magic( C ):
    n = len(C)
    res = [-1 for i in range(n)]
    res[0] = 0
    for i in range(n-1):
        if res[i] >= 0:
            g_on_floor = C[i][0]
            for j in range(1,4):
                if C[i][j][1] > i:
                    if res[i] + g_on_floor >= C[i][j][0] and g_on_floor - C[i][j][0] < 11:
                        res[C[i][j][1]] = max(res[i] + g_on_floor - C[i][j][0], res[C[i][j][1]])
    # tu prosze wpisac wlasna implementacje
    return res[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
