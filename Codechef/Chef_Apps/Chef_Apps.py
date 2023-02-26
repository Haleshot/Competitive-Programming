T = int(input())
while T:
    T -= 1
    S, X, Y, Z = map(int, input().split())
    remain = S - (X + Y)
    if Z <= remain:
        print(0)
    elif (S >= X + Z or S >= Y + Z):
        print(1)
    else:
        print(2)