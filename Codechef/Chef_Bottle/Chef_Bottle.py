T = int(input())
while T:
    T -= 1
    N, X, K = map(int, input().split())
    if X <= K:
        num = K//X
        if (num >= N):
            print(N)
        else:
            print(num)
    
    else:
        print(K//X)