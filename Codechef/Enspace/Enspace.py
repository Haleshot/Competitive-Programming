T = int(input())
while T:
    T -= 1
    N, X, Y = map(int, input().split())
    tot = X + 2 * Y
    if tot > N:
        print("NO")
    else:
        print("YES")
