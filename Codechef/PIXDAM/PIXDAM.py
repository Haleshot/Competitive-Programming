T = int(input())
while T:
    T -= 1
    H, W, X, Y, K = list(map(int, input().split()))
    if (((H - Y) * (H - Y)) + ((W - X) * (W - X))) ** 0.5 < K:
        print(1)
    else:
        print(0)
