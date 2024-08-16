T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    print((M * (M + 1) * N * (N + 1)) // 4 - (N * M))
