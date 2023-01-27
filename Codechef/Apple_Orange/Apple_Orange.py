T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    if (N + M) % 2 == 0:
        minimum = round((min(N, M)/2))
        print(minimum)
