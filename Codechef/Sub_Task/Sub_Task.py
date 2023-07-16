T = int(input())
while T:
    T -= 1
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    one_count = 0
    for i in A:
        if i == 1:
            one_count += 1      
            if (one_count == N):
                print(100)
        elif i == 0:
            if (one_count >= M):
                print(K)
            else:
                print(0)
        