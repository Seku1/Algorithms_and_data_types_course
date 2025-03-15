# Piotr Sękulski
# time complexity O(n) = n
# space complexity O(n) = n
# this algorithm is implementation of bucket sort algorithm because our data is continuous.
# First we create lists of heads and tails of each bucket, so we are creating bucket each bucket has a size of
# 10 divided by length of our array. Next we put every element in their correct bucket, finally we are connecting
# our bucket from last one to the first one
import random

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def printlist(a):
    while a is not None:
        print(a.val, ' --> ',end='')
        a = a.next
    print('END')


def list_to_linked(list):
    new = Node()
    for i in range(len(list)-1,-1,-1):
        new_node = Node(list[i], new.next)
        new.next = new_node
    # printlist(new)
    return new


def connect(heads, tails):
    res = Node()
    for i in range(len(heads)-1, -1, -1):
        # printlist(heads[i])
        if heads[i].next is not None:
            tails[i].next = res.next
            res = heads[i]
            # printlist(res)
    return res


def bucket_on_linked(p):
    n = 0
    curr = p.next
    heads = []
    tails = []
    while p is not None:
        p = p.next
        n += 1
        heads.append(Node())
        tails.append(Node())
    l_ran = 10 / n
    while curr is not None:
        # print(curr.val)
        curr_buc = int(curr.val / l_ran)
        # print(curr_buc, curr.val)
        if heads[curr_buc].next is None:
            heads[curr_buc].next = curr
            tails[curr_buc] = heads[curr_buc].next
            curr = curr.next
            tails[curr_buc].next= None
            # print(heads == tails)
        else:
            # if in bucket in witch we want to put our element in we do insertion sort because number of
            # elements in that bucket should be small
            if tails[curr_buc].val < curr.val:
                tails[curr_buc].next = curr
                curr = curr.next
                tails[curr_buc] = tails[curr_buc].next
            else:
                curr_sort = heads[curr_buc]
                while curr_sort.next is not None and curr_sort.next.val < curr.val:
                    curr_sort = curr_sort.next
                next_node = curr_sort.next
                curr_sort.next = curr
                curr = curr.next
                curr_sort.next.next = next_node
    return connect(heads, tails)


arr = []
for i in range(10000000):
    arr.append(random.randint(0,100000000000000000)/10000000000000000)
list = list_to_linked(arr)
# printlist(list)
print(1)
printlist(bucket_on_linked(list))
