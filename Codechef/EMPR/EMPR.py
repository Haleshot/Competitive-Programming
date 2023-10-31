T = int(input())
while T:
    T -= 1
    P, X, Y, Z = map(int, input().split())
    if Z == 1:
        P = P+ ( (P * Y) / 100)
    else:
        P = P - ((P * X / 100))
    print('{0:.10f}'.format(P))