T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if (15 * X) >= (2 * Y):
        print("YES")
    else:
        print("NO")