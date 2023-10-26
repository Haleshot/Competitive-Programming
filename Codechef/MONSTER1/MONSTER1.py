T = int(input())
while T:
    T -= 1
    H, X, Y = map(int, input().split())
    if (Y >= X):
        print(1)
    else:
        print(0)