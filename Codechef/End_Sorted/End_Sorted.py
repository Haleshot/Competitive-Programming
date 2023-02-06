T = int(input())
while T:
    T -= 1
    N = int(input())
    P = list(map(int, input().split()))
    c = 0
    if (P[0] == 1 and P[N - 1] == N):
        print(c)
    else:
        for i in range(N - 1):
            if P[i] > P[i + 1]:
                P[i], P[i + 1] = P[i + 1], P[i]
                c += 1
        if (P[0] == 1 and P[N - 1] == N):
            print(c)
