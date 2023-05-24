T = int(input())
while T:
    T -= 1
    X, Y, K = map(int, input().split())
    if X <= Y:
        least = (Y - X)//K
    elif X >= Y:
        least = (X - Y)//K
    else:
        print(0)
    print(least)