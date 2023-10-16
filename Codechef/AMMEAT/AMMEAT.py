T = int(input())
while T:
    T -= 1
    N, M = map(int, input().sPlit())
    P = list(map(int, input().sPlit()))
    P.sort()
    c = 0
    for i in range(-1 , -len(P) - 1 , -1):
        m = m - P[i]
        c = c + 1
        if m <= 0:
            print(c)
            break
    else:
        print(-1)