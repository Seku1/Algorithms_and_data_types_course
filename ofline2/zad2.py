# Piotr Sękulski nr albumu 422337
# Złożóność asymptyczna O(n) = p * n * log(p)
# Złożóność pamięciowa O(p) = p
# algorytm na początku sortuje na osobnej liście p elemętów dodawaniu k-tego od końca elemętu od wyniku,
# następnie usuwany jest i-ty elemęt z dużej tablicy z tej posortowanej indeks znajdywany jest za pomocą algorytmu
# binsearchu a następnie znajdowany jest za pomocą tego samego algorytmu miejsce na które ma być
# wstawiony p+i-ty elamęt i wstawianie go na to miejsce
from zad2testy import runtests


def merge(p, q, res):
    i, j = 0, 0
    while i < len(p) and j < len(q):
        if p[i] < q[j]:
            res[i+j] = p[i]
            i += 1
        else:
            res[i+j] = q[j]
            j += 1
    if len(p) == i:
        return res[:i + j] + q[j:]
    return res[:i + j] + p[i:]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[mid:]), merge_sort(arr[:mid]), arr)


def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2
        if x == arr[mid]:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def remove(arr, x):
    arr.pop(binary_search(arr, x))


def insert(arr, x):
    split = binary_search(arr, x) + 1
    arr[split:split] = [x]


def ksum(T, k, p):
    n = len(T)
    i = 0
    s_tab = T[:p]
    s_tab = merge_sort(s_tab)
    res = s_tab[p-k]
    while i + p < n:
        remove(s_tab, T[i])
        insert(s_tab, T[p+i])
        res += s_tab[p-k]
        i += 1
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
