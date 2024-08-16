T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    ans1 = 500 - 2 * X + 1000 - 4 * (X + Y)
    ans2 = 500 - 2 * (X + Y) + 1000 - 4 * Y
    print(max(ans1, ans2))
