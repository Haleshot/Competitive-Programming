T = int(input())
while T > 0:
    T -= 1
    N, K = map(int, input().split())
    l = list(map(int, input().split()))
    if len(l) == N:
        for i in l:
            if i <= K:
                K -= i
                print(1, end = "")
            else:
                print(0)
