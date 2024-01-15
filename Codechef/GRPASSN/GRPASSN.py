T = int(input())
while T:
    T -= 1
    N = int(input())
    P = list(map(int, input().split()))
    c = 0
    for i in range(N):
        if P[i] != P.count(P[i]):
            c += 1
    if c > 0:
        print("NO")
    else:
        print("YES")