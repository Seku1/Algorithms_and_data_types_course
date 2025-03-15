# Piotr Sękulski nr albumu 422337
# ten kod ma złożoność Θ(nlogk)
# ideą tego rozwiązania jest podzielenie listy na n/k k elemętowych fragmętów posortowanie ich algorytmem merge sortu
# dlatego ma w złożoności logk zamiast jak zwykły merge sort logn. następnie nabierząco podczas usyskiwania kolejnych
# fragmętów łączenie ich a następnie znajdywanie ich środka i łączenia ich od środka danego kawałka jako początku
# łączenia dla kolejnych kawałków ten  pomysł działa dlatego że elemęty listy mogą różnić się o conajmniej k elemętów
# a więc nieposortowany będzie po połączeniu tylko 2 połowa posortowanego kawałka i możemy łączyć kolejny
# od połowy połączonego kawałka


from zad1testy import Node, runtests


def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    head = Node()
    head.next = p
    prev = p
    curr = p
    mid = None
    cnt = 1
    flag = True
    while curr is not None:
        if cnt == 2 * k:
            flag = False
            tail = curr
            curr = curr.next
            tail.next = None
            prev = merge_sort(prev)
            if mid is not None:
                prev = merge(mid, prev)
            else:
                head.next = prev
            mid = f_mid(prev)
            prev = curr
            cnt = k + 1
        else:
            cnt += 1
            curr = curr.next
    prev = merge_sort(prev)
    prev = merge(mid,prev)
    if flag:
        head.next = prev
    return head.next


    pass


def merge(left, right):
    head = None
    tail = None
    if left is None or right is None:
        head = left
        if left is None:
            head = right
        return head
    while left is not None and right is not None:
        if head is None:
            if left.val < right.val:
                head = left
                tail = head
                left = left.next
            else:
                head = right
                tail = head
                right = right.next
        else:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
    tail.next = left
    if right is not None:
        tail.next = right
    return head


def f_mid(l_list):
    if l_list is None:
        return l_list
    slow = l_list
    fast = l_list.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sort(l_list):
    if l_list is None or l_list.next is None:
        return l_list
    mid = f_mid(l_list)
    left = l_list
    right = mid.next
    mid.next = None
    merged = merge(merge_sort(left), merge_sort(right))
    return merged


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
