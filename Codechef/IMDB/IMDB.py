T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    G = []
    for i in range(N):
        L = list(map(int, input().split()))
        if L[0] <= X:
            G.append(L[1])
    print(max(G))
