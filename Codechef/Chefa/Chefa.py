T = int(input())
while T:
    T -= 1
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    s = 0
    for i in range(N):
        if i % 2 == 0:
            s += L[i]
    print(s)
