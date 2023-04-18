T = int(input())
while T:
    T -= 1
    W, X, Y, Z = map(int, input().split())
    initial = W + X
    total = Y * Z
    if total > initial:
        print("Overflow")
    if total < initial:
        print("Unfilled")
    if total == initial:
        print("Filled")

