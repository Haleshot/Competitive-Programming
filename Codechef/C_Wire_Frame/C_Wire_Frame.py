T = int(input())
while T:
    T -= 1
    N, M, X = map(int, input().split())
    print(((X * ((2 * N) + (2 * M)))))