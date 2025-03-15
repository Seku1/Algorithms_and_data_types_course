#Piotr Sękulski 422337
# złożoność czasowa O(v) = v!
# złożóność pamięciowa O(n) = n
# algorytm działa na zasadziebackrtacingu w dfs, żeby program był szybszy zamieniłem reprezentacje grafu na
# listy sąsiedztwa

from zad4testy import runtests


def conv_to_adj_list(L):
    adj_mat = []
    for i in L:
        while len(adj_mat) < i[1] + 1:
            adj_mat.append([])
        # print(adj_mat)
        adj_mat[i[0]].append(([i[1], i[2]]))
        adj_mat[i[1]].append(([i[0], i[2]]))
    return adj_mat


def Flight(L,x,y,t):
    L = conv_to_adj_list(L)
    visited = [False] * len(L)

    def dfs(L, start, end, t, visited, min_alt=float("inf"), max_alt=float("0")):
        visited[start] = True
        if start == end:
            return True
        for eg in L[start]:
            if not visited[eg[0]]:
                if abs(max(max_alt, eg[1]) - min(min_alt, eg[1])) <= 2 * t:
                    if dfs(L, eg[0], end, t, visited, min(min_alt, eg[1]), max(max_alt, eg[1])):
                        return True
        visited[start] = False
        return False
    # tu prosze wpisac wlasna implementacje
    return dfs(L,x,y,t,visited)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
