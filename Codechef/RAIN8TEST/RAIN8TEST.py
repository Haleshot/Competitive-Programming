T = int(input())
while T:
    T -= 1
    N, X = list(map(int, input().split()))
    D = []
    cost = 0
    for j in range(N):
        D.append(int(input()))
    for i in range(len(D)):
        if D[i] == 1 or (i != 0 and D[i - 1] == 1):
            cost += X
    print(cost)
