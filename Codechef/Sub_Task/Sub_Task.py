T = int(input())
while T:
    T -= 1
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    one_count = A.count(1)
    zero_count = A.count(0)
    if (one_count == N):
        print(100)
    elif (one_count == M):
        print(K)
    else:
        print(0)