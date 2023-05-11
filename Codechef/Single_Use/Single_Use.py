import math
T = int(input())
while T:
    T -= 1
    H, X, Y = map(int, input().split())
    H -= Y
    attacks = math.ceil(H//X) + 1
    print(attacks)