T = int(input())
while T:
    T -= 1
    N = int(input())
    A = []
    for j in range(N):
        M = list(map(int, input().split()))
        A.append(M)
    for j in range(N - 2, -1, -1):
        for k in range(0, j + 1):
            A[j][k] += max(A[j + 1][k], A[j + 1][k + 1])
    print(A[0][0])
