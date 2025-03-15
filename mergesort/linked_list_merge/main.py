# merge sort on linked list
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def merge(list1, list2):
    # print_list(list1)# debugging
    # print_list(list2)
    # edge cases
    if list1 is None and list2 is None:
        return None
    if list1 is None:
        return list2
    if list2 is None:
        return list2
    head = None
    tail = None
    # start of merge
    while list1 is not None or list2 is not None:
        # print_list(head)    #debugging
        if list1 is not None and list2 is not None:
            if head is None:    # setting head in first iteration
                if list1.val < list2.val:
                    head = list1
                    tail = head
                    list1 = list1.next
                else:
                    head = list2
                    tail = head
                    list2 = list2.next
            else:    # attaching minimal number from both lists
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
        elif list1 is not None:   # ending merge if one of lists came to an end
            if head is None:
                return list1
            else:
                tail.next = list1
            # print_list(head)    # debugging
            # print()
            return head
        elif list2 is not None:
            # print(2)
            if head is None:
                return list2
            else:
                tail.next = list2
            # print_list(head)    # debugging
            # print()
            return head


def from_array_to_linked_list(arr):    # converting array to list out of convenience
    head = Node()    # setting guardian
    for i in range(len(arr)-1,-1,-1):     # part when I convert
        node = Node(arr[i], head.next)
        head.next = node
    return head.next


# function to print linkedlist
def print_list(head):
    while head is not None:
        print(head.val, "-->", end='')
        head = head.next
    print('End')


def find_middle(head):    # finding middle using method of tortoise and rabbit
    if head is None:
        return None
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergesort(head):
    # print(1)
    if head is None or head.next is None:
        return head
    mid = find_middle(head)
    head2 = mid.next
    mid.next = None
    final_head_1 = mergesort(head)
    final_head_2 = mergesort(head2)
    final_head = merge(final_head_1, final_head_2)
    # print_list(final_head)
    return final_head


if __name__ == '__main__':
    import random

    # print(arr)
    list1 = from_array_to_linked_list(arr)
    # print_list(list1)
    list2 = mergesort(list1)
    print_list(list2)