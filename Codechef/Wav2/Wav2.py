import bisect
N, Q = map(int, input().split())
B = sorted([int(x) for x in input().split()])
for _ in range(Q):
    x = int(input())
    c = bisect.bisect_left(B, x)
    if c < N and B[c] == x:
        print("0")
    elif c == N or (N - 1 - c) %2 != 0:
        print("POSITIVE")
    else:
        print("NEGATIVE")