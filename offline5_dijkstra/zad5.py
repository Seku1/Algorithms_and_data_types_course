from zad5testy import runtests
from queue import PriorityQueue
# Piotr Sękulski 422337
# Złożoność Obiiczeniowa O(ElogV)
# Ten algorytm jest implemętacją algorytmu djikstry bez implementacji parentów. Osobliwośći połączone są cyklem
# każda krawędz w tym cyklu ma wage 0

def conv_to_adj(graph, sing, n): # zmiana reprezentacji grafu na listę somsiedztwa
    adj = [[] for _ in range(n)]
    for u, v, t in graph:
        adj[u].append([v, t])
        adj[v].append([u, t])
    if len(sing) > 1:
        for i in range(len(sing)-1):
            adj[sing[i]].append([sing[i+1], 0])
        adj[sing[-1]].append([sing[0], 0])
    return adj


def spacetravel( n, E, S, a, b ):    # Tak naprawde w tej funkcji jest napisany algorytm djikstry
    E = conv_to_adj(E, S, n)
    Q = PriorityQueue()
    dist = [float("inf")] * n    # inicjacja algorytmu
    dist[a] = 0
    Q.put((dist[a], a))
    while not Q.empty():
        curr_dist, a = Q.get()
        for v in E[a]:
            if dist[v[0]] > curr_dist + v[1]:    # funkcja relax z wykładu
                dist[v[0]] = dist[a] + v[1]
                Q.put((dist[v[0]],v[0]))
    # tu prosze wpisac wlasna implementacje
    if dist[b] == float("inf"):
        return None
    return dist[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )