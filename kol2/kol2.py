from kol2testy import runtests
from queue import Queue

# algorytm polega na szukaniu najktótszej ścieżki w grafie bfsem przez co osiągana jest zlożonośc v + e bo krawędzie mają wagę do 16
def bfs(graph, start, end):
    visited = [False for _ in range(len(graph))]
    visited[start] = True
    queue = Queue()
    queue.put([0, start, 0, 0, 0])
    # (czas do końca odpoczynku,curr_v, czas trasy, czas do odpoczynku, wynik)
    while not queue.empty():
        rest, node, time, t_to_rest, res = queue.get()
        if rest == 0:
            if time != 0:

                if end == node:
                    # print(parent)
                    return res
                for v in graph[node]:
                    if not visited[v[0]]:
                        print(res, node)
                        time = v[1]
                        t_to_rest += time
                        res += time
                        if t_to_rest > 16:
                            res += 8
                            t_to_rest = 0
                        visited[v[0]] = True
                        queue.put([rest, v[0], time, t_to_rest, res])
            else:
                time -= 1
                queue.put([rest, node, time, t_to_rest, res])

        else:
            rest -= 1
            queue.put([rest, node, time, t_to_rest, res])


def to_adj_list(graph):
    adj_list = []
    for v, w, val in graph:
        while len(adj_list) < w + 1 or len(adj_list) < v + 1:
            adj_list.append([])
        adj_list[w].append([v, val])
        adj_list[v].append([w, val])
    return adj_list



def warrior( G, s, t):
    G = to_adj_list(G)
    # tu prosze wpisac wlasna implementacje
    return bfs(G, s, t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
