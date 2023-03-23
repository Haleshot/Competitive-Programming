import math
T = int(input())
while T:
    T -= 1
    X = int(input())
    temp = math.ceil(X/3)
    temp *= 3
    print(temp - X)