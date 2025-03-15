from egz1btesty import runtests


class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
    # tu prosze wpisac wlasna implementacje
    leafs = [1, 0]
    curr_stack = [T]
    next_stack = []
    j = 0
    while len(curr_stack) > 0:
        if len(curr_stack) >= leafs[0]:
            leafs = [len(curr_stack), j]
        for i in range(len(curr_stack)):
            if curr_stack[i].left is not None:
                next_stack.append(curr_stack[i].left)
            if curr_stack[i].right is not None:
                next_stack.append(curr_stack[i].right)
        j += 1
        curr_stack = next_stack
        next_stack = []

    best_level = leafs[1]

    def dfs(x, time, level):
        to_cut = 0
        if time == level:
            if x.left is not None:
                to_cut += 1
            if x.right is not None:
                to_cut += 1
            return to_cut
        if x.left is None and x.right is None:
            return -1
        elif x.left is not None and x.right is not None:
            left = dfs(x.left, time + 1, level)
            right = dfs(x.right, time + 1, level)
            if left < 0 and right < 0:
                return -1
            elif left >= 0 and right < 0:
                return right + 1
            elif left < 0 and right >= 0:
                return left + 1
            else:
                return right + left

        elif x.left is not None and x.right is None:
            return dfs(x.left, time + 1, level)
        elif x.right is not None and x.left is None:
            return dfs(x.right, time + 1 ,level)

    return dfs()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )