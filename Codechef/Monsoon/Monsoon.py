T = int(input())
while T:
    T -= 1
    N, M, H = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    NM_min = min(N, M)

    X.sort(reverse=True)
    Y.sort(reverse=True)

    c = 0

    for i in range(NM_min):
        if X[i] < (Y[i] * H):
            c = c + X[i]
        else:
            c = c + (Y[i] * H)
    print(c)
