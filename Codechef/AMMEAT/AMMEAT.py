T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    c = 0
    for i in range(-1, -len(P) - 1, -1):
        M -= P[i]
        c = c + 1
        if M <= 0:
            print(c)
            break
    else:
        print(-1)
