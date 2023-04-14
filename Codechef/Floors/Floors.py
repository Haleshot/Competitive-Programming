T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if X % 10 == 0 and Y % 10 == 0:
        print(X - Y)
    else:
        pass