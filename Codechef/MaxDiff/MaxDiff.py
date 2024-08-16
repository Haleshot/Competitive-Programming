T = int(input())
while T:
    T -= 1
    N, S = map(int, input().split())
    t1 = min(N, S)
    t2 = S - t1
    max_diff = t1 - t2
    print(max_diff)
