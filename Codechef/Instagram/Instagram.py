T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if Y >= 10 * X:
        print("YES")
    else:
        print("NO")