T = int(input())
while T:
    T -= 1
    N, K = map(int, input().split())
    W = list(map(int, input().split()))
    W.sort()
    sum_kid, sum_Chef = 0, 0
    print(W)
    # sum_kid = [i for i in W[0:K]]
    for i in range(K + 1):
        sum_kid += 1
    for i in range(K, N + 1):
        sum_Chef += 1

    print(sum_Chef, " ", sum_kid)
    # print(sum_Chef - sum_kid)