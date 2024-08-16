T = int(input())
while T:
    T -= 1
    X, Y, D = map(int, input().split())
    if abs(X - Y) <= D:
        print("YES")
    else:
        print("NO")
