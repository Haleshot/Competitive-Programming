T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if Y >= 0.5 * X:
        print("YES")
    else:
        print("NO")
