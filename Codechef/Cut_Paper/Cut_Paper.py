T = int(input())
while T:
    T -= 1
    N, K = map(int, input().split())
    print((N//K) * (N//K))