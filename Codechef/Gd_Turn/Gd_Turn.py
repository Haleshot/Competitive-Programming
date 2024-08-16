T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if X + Y > 6:
        print("YES")
    else:
        print("NO")
