T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    c = 0
    for i in range(1, N + 1, 2):
        for j in range(1, M + 1, 2):
            c += 1
    print(c)