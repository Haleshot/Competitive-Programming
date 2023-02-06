T = int(input())
while T:
    T -= 1
    N = int(input())
    P = list(map(int, input().split()))
    c = 0
    if (P[0] == 1 and P[N - 1] == N):
        print(c)
        print()
    else:
        index_1 = P.index(1)
        index_n = P.index(N)
        if (P[0] == 1 and P[N - 1] == N):
            print(c)
            print()
