T = int(input())
while T:
    T -= 1
    N, A, B = map(int, input().split())
    S = []
    c1, c2 = 0, 0
    for i in range(N):
        S.append(input())
    for i in S:
        if i[0] in "EQUINOX":
            c1 += A
        else:
            c2 += B
    if c1 > c2:
        print("SARTHAK")
    elif c1 < c2:
        print("ANURADHA")
    else:
        print("DRAW")
