T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    c = 0
    for i in range(N):
        if A[i] >= X:
            c += B[i]
    print(c)
