T = int(input())
while T:
    T -= 1
    W, X, Y, Z = map(int, input().split())
    c = Y * Z
    total = W + c
    if total > X:
        print("Overflow")
    if total < X:
        print("Unfilled")
    if total == X:
        print("Filled")

