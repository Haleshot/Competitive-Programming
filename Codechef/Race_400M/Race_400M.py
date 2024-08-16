T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    X = 400 / X
    Y = 400 / Y
    Z = 400 / Z
    if X > Y and X > Z:
        print("ALICE")
    elif Y > X and Y > Z:
        print("BOB")
    elif Z > X and Z > Y:
        print("CHARLIE")
