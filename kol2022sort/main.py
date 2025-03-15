def bin_search(arr, el):
    if len(arr) == 0:
        return 0
    p = 0
    q = len(arr)-1
    mid = q // 2
    while p < q:
        mid = (p + q) // 2
        if el == arr[mid]:
            return mid
        elif arr[mid] < el:
            q = mid - 1
        else:
            p = mid + 1
    return mid


def cnt_sort(arr):
    if len(arr) == 0:
        return 0
    n = len(arr) - 1
    cnt = [1]
    elem = [arr[0]]
    m_cnt = 1
    for i in range(n+1):
        arr[i] = max(arr[i], arr[i][::-1])
        # print(bin_search(elem,arr[i]))
        index = bin_search(elem, arr[i])
        if elem[index] == arr[i]:
            cnt[index] += 1
            m_cnt = max(m_cnt, cnt[index])
        else:
            # print(index)
            elem.insert(index, arr[i])
            cnt.insert(index, 1)
    return m_cnt


T = ['pies', 'kogut', 'mysz', 'kot', 'tok', 'seip','kot']

print(cnt_sort(T))