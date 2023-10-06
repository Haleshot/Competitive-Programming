T = int(input())
while T:
    T -= 1
    N, K = map(int, input().split())
    if N >= K and K != 0:
        print(N % K)
    else:
        print(N)