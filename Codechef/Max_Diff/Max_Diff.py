T = int(input())
while T:
    T -= 1
    N, K = map(int, input().split())
    Q = min(N - K, K)
    W = list(map(int, input().split()))
    W.sort()
    sum_kid, sum_Chef = sum(W[:Q]), sum(W[Q:N])
    print(sum_Chef - sum_kid)
