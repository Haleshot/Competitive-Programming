T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if ((X == Y) and (X != 0 and Y != 0)):
        print("YES")
    else:
        print("NO")