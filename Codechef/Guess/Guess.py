T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    l = []
    for i in range(1, N):
        for j in range(1, M):
            l.extend([[i, j]])
            print(l)