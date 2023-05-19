T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    if N < M:
        print(N)
    else:
        print((N - M) + N)