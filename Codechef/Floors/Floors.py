import math

T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    x = math.ceil(X / 10)
    y = math.ceil(Y / 10)
    print(abs(x - y))
