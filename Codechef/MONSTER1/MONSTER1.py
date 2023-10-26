T = int(input())
while T:
    T -= 1
    H, X, Y = map(int, input().split())
    if (Y >= X):
        print(0)
    else:
        print(1)