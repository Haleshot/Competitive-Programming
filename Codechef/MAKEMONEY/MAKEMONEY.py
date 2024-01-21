T = int(input())
while T:
    T -= 1
    N, X, C = map(int, input().split())
    A = list(map(int, input().split()))
    c = 0
    for i in range(N):
        if A[i] < X and (X - A[i] > C):
            A[i] = X
            c += 1
    print(sum(A) - (c * C))