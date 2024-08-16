T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    LHS = X**4 + (4 * Y**2)
    RHS = 4 * (X**2 * Y)
    if LHS == RHS:
        print("YES")
    else:
        print("NO")
