T = int(input())
while T:
    T -= 1
    N = int(input())
    S = [0] * 8
    for j in range(N):
        X, Y = map(int, input().split())
        if X <= 8:
            S[X - 1] = max(S[S - 1], Y)
    print(sum(S))