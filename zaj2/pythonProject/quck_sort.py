# niedziała

def quickSort(arr, p, k):
    while p < k:
        x = arr[k-1]
        i = p
        j = p
        while j < k-1 :
            if arr[j] < x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1
        arr[i], arr[k-1] = arr[k-1], arr[i]
        quickSort(arr, p, i-1)
        quickSort(arr, i+1,k)

arr = [10, 8, 7, 6, 5, 4, 3, 2, 1]
quickSort(arr, 0, len(arr))
print(arr)