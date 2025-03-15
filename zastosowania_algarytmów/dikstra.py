def dijkstra(graph, st):
    to_check = PriorytyQueue()
    v = len(graph)
    to_check.put((0,st))
    dist = [float('inf')] * v
    dist[st] = 0
    parent = [None] * v
    while not to_check.empty():
        curr_dist, v = to_check.get()
        for neighbor, c in graph[v]:
            dist[neighbor] = curr_dist + c
            parent[neighbor] = v
            to_check.put((dist[neighbor], neighbor))