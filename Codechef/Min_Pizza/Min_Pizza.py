import math
T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    slices = N * X
    print(math.ceil(slices/4))