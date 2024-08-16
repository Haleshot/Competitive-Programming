import math

T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if Y <= Z:
        print(X)
    else:
        print(X * math.ceil(Y / Z))
