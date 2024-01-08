T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if (X + Y == Z or Y + Z == X or Z + X == Y):
        print("YES")
    else:
        print("NO")