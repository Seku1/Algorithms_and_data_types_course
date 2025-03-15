def sciag(T,A):
    F = [0]
    for i in range(len(T)):
        F[0][i] = True
    for i in range(m):
        for j in range(n):
            F[i][j] = F[i-A[i]][i-1] or F[i][i-1]
    return F[T][n-1]