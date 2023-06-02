T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if Y > X:
        print("PROFIT")
    elif Y < X:
        print("LOSS")
    else:
        print("NEUTRAL")