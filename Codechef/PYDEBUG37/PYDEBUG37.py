T = int(input())
while T:
    T -= 1
    S, X, Y, Z = map(int, input().split())
    if (S - X - Y) >= Z:
        print(0)
    else:
        if (S - min(X, Y)) >= Z:
            print(1)
        else:
            print(2)
