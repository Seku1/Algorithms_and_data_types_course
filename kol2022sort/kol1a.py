from kol1atesty import runtests


def bin_search(arr, el):

    p = 0
    q = len(arr)-1
    mid = q // 2
    while p <= q:
        # print(1)
        mid = (p + q) // 2
        if el == arr[mid]:
            return mid
        elif arr[mid] < el:
            p = mid + 1
        else:
            q = mid - 1
    return mid


def cnt_sort(arr):
    if len(arr) == 0:
        return 0
    n = len(arr) - 1
    cnt = [0]
    elem = [max(arr[0], arr[0][::-1])]
    m_cnt = 1
    for i in range(n+1):
        arr[i] = max(arr[i], arr[i][::-1])

        # print(bin_search(elem,arr[i]))
        index = bin_search(elem, arr[i])
        if elem[index] == arr[i]:
            cnt[index] += 1
            m_cnt = max(m_cnt, cnt[index])
        else:
            if arr[i] in elem: print(1, end='')
            if arr[i]<elem[index]:
                elem.insert(index, arr[i])
                cnt.insert(index, 1)
            else:
                elem.insert(index+1, arr[i])
                cnt.insert(index+1, 1)
        # print(elem)
    return m_cnt


def g(T):
    # tu prosze wpisac wlasna implementacje
    return cnt_sort(T)


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
