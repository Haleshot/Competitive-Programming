T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if (5 * X >= Y):
        print("YES")
    