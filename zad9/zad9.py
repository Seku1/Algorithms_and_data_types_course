from zad9testy import runtests


def trip(M):

  def dfs(T, M, v_x, v_y):
    n = len(M)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    childs = []
    for i, j in moves:
      if 0 <= v_x + i < n and 0 <= v_y + j < n and M[v_x + i][v_y + j] > M[v_x][v_y]:
        if T[v_x + i][v_y + j] < 0: childs.append(dfs(T, M, v_x + i, v_y + j))
        else: childs.append(T[v_x + i][v_y + j])
    if len(childs) > 0:
      T[v_x][v_y] = max(childs) + 1
    else:
      T[v_x][v_y] = 1
    return T[v_x][v_y]

  score = 0
  n = len(M)
  T = [[-1 for i in range(n)] for j in range(n)]
  for i in range(n):
    for j in range(n):
      if T[i][j] < 0:
        dfs(T, M, i, j)
        score = max(score, T[i][j])
  return score

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
