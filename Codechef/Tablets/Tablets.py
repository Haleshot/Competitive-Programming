T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if 3 * X <= Y:
        print("YES")
    else:
        print("NO")
