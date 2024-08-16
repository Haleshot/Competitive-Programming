T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    count = 0
    A = (500 - 2 * X) + (1000 - 4 * (X + Y))
    B = (1000 - 4 * Y) + (500 - 2 * (X + Y))
    if A > B:
        print(A)
    else:
        print(B)
