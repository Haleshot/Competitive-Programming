T = int(input())
while T:
    T -= 1
    N, K, V = map(int, input().split())
    A = list(map(int, input().split()))
    result = ((V * (N + K)) - sum(A))/K
    if result > 0:
        print(result)
    else:
        print(-1)