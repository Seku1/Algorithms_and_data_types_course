from egzP1btesty import runtests 
from queue import PriorityQueue
def turysta( G, D, L ):
    inf = float("inf")
    graph = []
    n = len(G)
    for u, v, w in G:
        while len(graph) - 1 < v:
            graph.append([])
        graph[u].append([v, w])
        graph[v].append([u, w])
    arr = [[inf, inf, inf, inf] for _ in range(len(graph))]
    arr[0] = [0, 0, 0, 0]
    def dijkstra(graph, arr):
        q = PriorityQueue()
        q.put((arr[0], -1, 0))
        while not q.empty():
            res, turn, v = q.get()
            turn += 1
            if turn > 3:
                continue
            for u, w in graph[v]:
                if turn == 3 and u != L: continue
                if u ==L and turn > 3: continue
                if arr[u][turn] > res[turn-1] + w:
                    # print(arr[u], res, w, turn, u, v)
                    arr[u][turn] = res[turn-1] + w
                    # print(arr[u], res)
                    q.put((arr[u], turn, u))


    dijkstra(graph, arr)
    # for i in range(len(arr)):
    #     print(i, arr[i])


    #tutaj proszę wpisać własną implementację
    return arr[L][3]

runtests ( turysta )