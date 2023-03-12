T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    time = 1.07 * X
    if (Y > time):
        print("NO")
    else:
        print("YES")