# Piotr Sękulski 422337
# złożoność obliczeniowa algorytmu O(n) = n
# złożónść pamięciowa algorytmu O(n) = n
# algorytm działa na zasadzie counting sortu funkcja count najpierw liczy ile punktów stoi na jakiejś pozycji x/y
# następnie funkcja how_many_to_dominate zmienia wartości w tej tablicy na to ile punktów nie znajduje się w przedziale
# dominacji współżędnych x/y następnie w pentli for w funkcji dominance  zlicza odejmuje od liczby punktów tyle ile nie
# znajduje się w przedziale dominacji x/y to rozwiązanie nie zlicza podwójnie dominacji punktów bo
# punkt który ma współżędne x i y większe od tego punktu dominuje ten punkt z większymi współżęndnymi
# więc i tak ilość ptk dominowanych przez ten jest mniejsza od ilości tego 2 punktu
from zad3testy import runtests


def count(x, y, arr):
 for element in arr:
  x[element[0] - 1] += 1
  y[element[1] - 1] += 1


def how_many_to_dominate(x, y):
 n = len(x)
 cnt_x = n
 cnt_y = n
 for i in range(n):
  cnt_x, x[i] = cnt_x - x[i], cnt_x
  cnt_y, y[i] = cnt_y - y[i], cnt_y


def dominance(P):
 n = len(P)
 cnt_x = [0] * n
 cnt_y = [0] * n
 count(cnt_x, cnt_y, P)
 how_many_to_dominate(cnt_x, cnt_y)
 h_domin = 0
 for element in P:
  curr_domin = n + 1
  curr_domin -= (cnt_y[element[1]-1] + cnt_x[element[0]-1])
  h_domin = max(h_domin, curr_domin)
 return h_domin


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = False )
