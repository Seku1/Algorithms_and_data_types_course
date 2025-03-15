# Algorytm mergesortu
import random
#podfunkcja łącząca dwie posortowane tablice
def merge(left, right, m_into):
    n = len(left)
    m = len(right)
    i, j = 0, 0
    # print(m_into, left, right)
    while i < n or j < m:
        if i < n and j < m:    # sprawdza czy i, j nie wychodzą poza tablice
            if left[i] < right[j]:    # sprawdza która wartość jest mniejsza i umieszcza ją w tabilcy
                m_into[i+j] = left[i]
                i += 1
            else:
                m_into[i+j] = right[j]
                j += 1
        elif i < n and j == m:
            # print(m_into)
            m_into[i + j] = left[i]
            i += 1
        elif j < m and i == n:
            m_into[i + j] = right[j]
            j += 1
    # print(m_into)
    return m_into


def merge_sort(tab):
    n = len(tab)
    if n == 1:
        # print(tab)
        return tab
    return merge(merge_sort(tab[:n//2]), merge_sort(tab[n//2:]), tab)


if __name__ == '__main__':
    arr = list(range(10000000))
    random.shuffle(arr)
    print(merge_sort(arr))