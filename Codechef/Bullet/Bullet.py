T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    t = Y//X
    if (Z > t):
        print(Z - t)
    else:
        print("0")