from kol2atesty import runtests


class find_union:
    def __init__(self, value):
        self.val = value
        self.parent = self
        self.rank = 0

    def find(self):
        if self.parent != self:
            self.parent = self.parent.find()
        return self.parent

    def union(self,y):
        x = self.find()
        y = y.find()
        if x.rank > y.rank:
            x.parent = y
            y.rank += 1
        else:
            x.parent = y
            x.rank += 1

    def can_add(self, y, z = None):
        x = self.find()
        y = y.find()
        if z is not None:
            z = z.find()
            if x.rank + y.rank + z.rank < 3: return True
        else:
            if x.rank + y.rank < 3: return True
        return False

def drivers( P, B ):
    # tu prosze wpisac wlasna implementacje

    def make_w_graph(P, B):
        n = len(P)
        arr = []
        wage = 0
        for i in range(B):
            if i > n - 1:
                arr.append((B, wage, len(arr) - 1))
                break
            if P[i][1]:
                arr.append((i, wage, len(arr) - 1))
                wage = 0
            else:
                wage += 1
        return arr[1:]

    def take_greedy(G):
        n = len(G)
        if n == 0:
            return []
        result = []
        arr = [find_union(i[2]) for i in G]
        arr[0].rank += 1
        print(G)
        G.sort(key=lambda v: v[1], reverse=True)
        for w, place, i in G:
            print(w, place, i)
            # print(i)
            cand = arr[i]
            if 0 < i < n - 1 and cand.can_add(arr[i - 1], arr[i + 1]):
                result.append(place)
                cand.union(arr[i - 1])
                cand.union(arr[i + 1])
            elif 0 < i and cand.can_add(arr[i - 1]):
                result.append(place)
                cand.union(arr[i - 1])
            elif i < n - 1 and cand.can_add(arr[i + 1]):
                result.append(place)
                cand.union(arr[i + 1])
        return result

    graph = make_w_graph(P, B)
    return take_greedy(graph)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )


