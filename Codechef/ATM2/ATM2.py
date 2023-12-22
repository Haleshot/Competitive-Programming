T = int(input())
while T:
    T -= 1
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    tid = []
    for i in range(N):
        if A[i] <= K:
            K -= A[i]
            tid.append(1)
        else:
            tid.append(0)
    print(*tid, sep="")