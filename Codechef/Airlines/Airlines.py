T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    limit = 10 * X
    if limit < Y:
        print(limit * Z)
    else:
        print(Y * Z)
