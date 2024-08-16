T = int(input())
while T:
    T -= 1
    A, B, C, D = list(map(int, input().split(" ")))
    E = (100 + D) / 100 * A
    if E >= B and E <= C:
        print("YES")
    else:
        print("NO")
