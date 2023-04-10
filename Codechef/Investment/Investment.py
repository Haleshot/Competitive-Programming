T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if X >= 2 * Y:
        print("YES")
    else:
        print("NO")