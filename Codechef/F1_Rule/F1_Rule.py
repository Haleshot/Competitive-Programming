T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    time = X + 1.7 * X
    if (Y > time):
        print("NO")
    else:
        print("YES")