from kol1testy import runtests
# Piotr Sękulski 422337
# złożoność asymptotyczna O(n) = nlog(n)
# algorytm na poczżtku przypisuje każdemu argumętowi jego indeks po posortowaniu, następnie wykonywane jest sortowanie
# merge sortem. Można zauważyć że jeśli odejmiemy od indeksu elemęlu przed posortowaniem ilość elemętów większych od
# tego elemętu to otrzymamy range denego elemętu jeśli ten elemęt ma szanse na zostanie elemętem który ma największą
# range. Dlatego po posrtowaniu wykonuje to co zaobserwowałem w ostatniej pentli for w funkcji maxrank. Jednak gdy w
# tablicy wystąpi ten sam elemęt to elemęt najbardziej na prawo od tego elemętu się powtuży to jest ten wynik zakłamamy
# przez ilość powtużeń tego elemętu, na ten problem odpowiada warunek if w 18 lini kodu. Przez ten warunek brzegowy
# używam również stabilnego mergesorta żeby nie zmienić kolejności tych powtużonych elemętów


def merge(res, p, q):
  n, m = len(p), len(q)
  i, j = 0, 0
  while i + j < n + m:
    if i < n and j < m and p[i][0] <= q[j][0]:
      if p[i][0] == q[j][0]: q[j][1] -= 1
      res[i + j] = p[i]
      i += 1
    elif i < n and j < m and p[i][0] > q[j][0]:
      res[i + j] = q[j]
      j += 1
    elif i < n and j == m:
      res[i + j] = p[i]
      i += 1
    elif j < m and i == n:
      res[i + j] = q[j]
      j += 1
  return res


def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  return merge(arr, merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def maxrank(T):
  n = len(T)
  for i in range(len(T)):
    T[i] = [T[i], i]
  merge_sort(T)
  max_cnt = 0
  for j in range(len(T)):
    i = T[j][1]
    cnt = i - (n - (j + 1))
    max_cnt = max(max_cnt, cnt)

  # tu prosze wpisac wlasna implementacje
  return max_cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
