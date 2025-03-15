# Piotr Sękulski 422337
# złożoność obliczeiowa O(n,m) = n*m
# złożoność pamięciowa O(n, m) = m
# algorytm działa na zasadzie funkcji z podpowiedzi. I obserwacji że musimy trzymać obserwacje z tylko dwóch rzędów
# tablicy wszystkich wyników
from zad8testy import runtests


def min(x, y):
  if x < y:
    return x
  return y


def parking(X,Y):
  # tu prosze wpisac wlasna implementacje
  inf = float('inf')
  n = len(X)
  m = len(Y)
  curr_arr = [inf for i in range(m)]

  for i in range(m - n + 1):
    curr_arr[i] = abs(X[0] - Y[i])
  for i in range(1, n):
    min_dist = inf
    arr_bef = curr_arr
    curr_arr = [inf for _ in range(m)]
    for j in range(i, m - n + i + 1):
      min_dist = min(min_dist, arr_bef[j-1])
      curr_arr[j] = abs(X[i] - Y[j]) + min_dist
  min_dist = inf
  for i in curr_arr:
    min_dist = min(min_dist, i)
  return min_dist


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
