import queue
from collections import deque


# def zad1(q,n):
#     q = deque()
#     visited_a = [False for _ in range(n)]
#     visited_b = [False for _ in range(n)]
#     q.appendleft((0, 'A'))
#     while len(q) > 0:
#         v, color = q.popleft()
#         if color == 'A':
#             if visited_b[v]: return False
#             if visited_a[v]: continue
#         else:
#             color = 'B'
#             if visited_a[v]: return False
#             if visited_a[v]: continue
#         for i in range(n):
#             if q[v][i] == 1:
#                 if color == 'A':
#                     q.append((i,'A'))
#                 else:
#                     q.append((i,'B'))
#             if color == 'B':
#                 visited_b[v] = True
#             else:
#                 visited_a[v] = True


# def zad_3(A):
#     n = len(A)
#     tab = [-n-1, -n, -n +1,-1,0, n-1, n, n+1]
#     B = [0]*(n**2)
#     q = queue
#     q.put(0)
#     for i in range(n):
#         for j in range(n):
#             B[i * n +j] = A[i][j]
#     visited = [0] * (n**2)
#     distance = [0] * (n**2)
#     parent = [0] * (n**2)
#     while q.empty():
#         porn = q.get()
#         for i in range (len(tab)):
#             if porn + tab[i] == 0:
#                 q.put(porn+tab[i])
#                 visited[porn + tab[i]] = 1
#                 parent[porn + tab[i]] = porn
#                 distance[porn + tab[i]] = distance[porn] + B[porn + tab[i]]
#     return distance[n**2-1]
#######################################################################################################################
#
#
# def zad1():
#     inf = float('inf')
#     def sol(g):
#         v = len(g)
#         dist = [[inf for _ in range(v)] for _ in range(v)]
#         for i in range(v):
#             dist[i][i] = 0
#         for v in range(v):
#             for i in range(v):
#                 if g[v][i] == 1:
#                     dist[v][i] = 0
#         for i in range(v):
#             for v in range(v):
#                 for n in range(v):
#                     if dist[v][n] == 1:
#                         continue
#                     dist[v][i] = dist[v][i] * dist[i][n]
#

class Node:
    def __init__(self, value):
        self.value = None
        self.parent = None