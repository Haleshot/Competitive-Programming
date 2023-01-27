def hcf(a, b):
    if (b == 0):
        return abs(a)
    else:
        return hcf(b, a % b)

T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    if (N + M) % 2 == 0:
        result = hcf(N, M)
        print(result)