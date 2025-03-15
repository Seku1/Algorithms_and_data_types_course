from egz1btesty import runtests
# Piotr Sękulski 422337
# Złożoność czasowa O(nk) pamięciowa O(nk)
# algorytm w idei ma przechodzić przez tablice T i wykonywać funkcie f(i, k) - maksymalna wartość maksymalnego dokładnie
# k spujnego ciągu dla indeksu i
# niestety niedziała



def kstrong(T, k):
  inf = float('inf')
  n = len(T)
  d_arr = [[-inf for i in range(n)] for j in range(k + 1)] # inicjalizacja tablicy dp
  d_arr[0][0] = T[0]
  for i in range(1, n):
    d_arr[0][i] = max(T[i], d_arr[0][i-1] + T[i]) # sprawdzanie czy suma elemętów całej tablicy do i-tego elemętu jest
    # większa od danego elementu jeśli nie to wybieramy nowy podciąg bo ten już nie jest opłacalny
    for j in range(1, k + 1):
      cand = max(d_arr[j-1][i-1], d_arr[j][i-1] + T[i]) # wybór kandydata na dane miejsce w tablicy albo pomijamy elemęt
      # k - 1 rzędu o indeksie i albo ciągniemy bez przerwy poprzedni wybór podciągu
      if cand > - inf:
        d_arr[j][i] = cand
  res = d_arr[0][n-1]
  for i in range(1, k+1):
    res = max(res, d_arr[i][n-1])
  return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
