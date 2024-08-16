T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if Y <= X:
        print(Y)

    else:
        print(X + 2 * (Y - X))
