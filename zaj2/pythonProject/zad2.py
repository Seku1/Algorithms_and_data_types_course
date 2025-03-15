def repair(T,i):

    if T[i] > T[parent(i)]:
        T[i], T[parent(i)] = T[parent(i)], T[i]
        repair(T,parent(i))

def add(i,T,n,k):
    T.append(i)






def parent(i):
    return (i-1)//2