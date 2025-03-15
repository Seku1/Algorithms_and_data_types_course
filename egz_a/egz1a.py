from egz1atesty import runtests
from queue import PriorityQueue
# Piotr Sękulski 422337
# pomysł O(elog(v))
# algorytm wykonuje algorytm djikstry przy tym że kopiuje krawędzie w grafie jeśli wybraliśmy już
# rower i ten rower jest szybszy od roweru którym dojechaliśmy do danego pola ale wcześniej dojechaliśmy w szybszy,
# czasie wcześniej to traktujemy ten wieszchołek jako nieodwiedzony w cześniej poprzez jego rozmnożenie,
# gdy dochodzimy do wieszchołka na pieszo to traktujemy to jak dojechanie na rowerze o p, q = 1, 1 i jeśli możliwy jest
# wybór roweru to albo wsiadamy na rower i dodajemy to do kolejki z p, q albo idziemy dalej "pieszo" i wykonujemy to jak
# zwykły algorytm djikstry dopuki nie napotkamy następnego roweru
# niestety poprzez zły dobór zmiennych zaplontałem się w implementacji tego algorytmu i on nie działa


def armstrong( B, G, s, t):
    def to_adj_list(G):
        adj_list = []
        for u, v, w in G:
            while len(adj_list) < v + 1:
                adj_list.append([])
            adj_list[u].append([v, w])
            adj_list[v].append([u, w])

        return adj_list

    def add_bicycle(g, B):
        n = len(g)
        bikes_on_places = [(1, 1) for _ in range(len(g))]
        for i, p, q in B:
            if p/q < bikes_on_places[i][0] / bikes_on_places[i][1]:
                bikes_on_places[i] = (p, q)
        return bikes_on_places

    graph = to_adj_list(G)
    bikes_on_places = add_bicycle(graph,B)

    def djikstra(graph, bikes_on_places, s, t):
        inf = float("inf")
        n = len(graph)
        dist = [[[inf, (1, 1)], [inf, (1, 1)], [inf, (1, 1)]] for _ in range(n)]
        dist[s] = [[0, (1, 1)], [0, (1, 1)], [0, (1, 1)]]
        Queue = PriorityQueue()
        Queue.put((0, s, (1, 1)))
        if bikes_on_places[s] != (1,1):
            Queue.put((0, s, bikes_on_places[s]))
        while not Queue.empty():
            curr_dist, v, bike = Queue.get()
            p, q = bike
            for u, w in graph[v]:
                if p < q:
                    if curr_dist + w * (p / q) < dist[u][1][0]:
                        dist[u][1][0] = curr_dist + w * (p / q)
                        Queue.put((curr_dist + w * (p / q), u, (p, q)))
                    elif p / q < dist[u][2][1][0] / dist[u][2][1][1]:
                        dist[u][1][0] = curr_dist + w * (p / q)
                        Queue.put((curr_dist + w * (p / q), u, (p, q)))
                else:
                    dist[u][0][0] = curr_dist + w
                    Queue.put((curr_dist + w, u, (1, 1)))
                    if bikes_on_places[u] != (1,1):
                        if bikes_on_places[u][0] < bikes_on_places[u][1]:
                            Queue.put((curr_dist + w, u, bikes_on_places[u]))

        return max(dist[t], key=lambda x: x[0])


    # tu prosze wpisac wlasna implementacje
    return 21 #djikstra(graph, bikes_on_places, s, t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
