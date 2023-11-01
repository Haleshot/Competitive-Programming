import math
T = int(input())
while T:
    T -= 1
    N, X1, X2, X3, X4, X5, X6 = list(map(int, input().split()))
    X = (X1 + X2 + X3 + X4 + X5 + X6 ) * math.ceil((N / 2))
    print(X)