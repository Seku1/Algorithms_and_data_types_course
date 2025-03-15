class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert (first, value):
    if first is None:
        return first
    a = first
    while a.next is not None:
        if a.val == value:
            return first
        elif a.next < value:
            nast = a.next
            a.next = value
            a.next.next = nast
            return first
    if value > a.next.val: a.next = value
    return first


def sort(first):
    limit = float("inf")
    if first is None:
        return first
    current = first
    new_list = None
    while current:
        value = current.val
        new_list = insert(new_list, value)
        current = current.next
    return new_list
