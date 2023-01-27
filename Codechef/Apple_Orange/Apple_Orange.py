import math
T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    if (N + M) % 2 == 0:
        if N % 2 == 0 or M % 2 == 0:
            print(min(N, M)/2)

        elif N % 2 == 1 or M % 2 == 1:
            minimum = math.ceil((min(N, M)/2))
            print(minimum)
