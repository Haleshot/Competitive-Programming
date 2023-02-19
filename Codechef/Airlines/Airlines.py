T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    num = 10 * X
    if (num < Y):
        print(num * Z)
    else:
        print(Y * Z)