T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if (400//X) > ((400//Y) and (400//Z)):
        print("ALICE")

    elif (400//Y) > ((400//X) and (400//Z)):
        print("BOB")

    elif (400//Z) > ((400//X) and (400//Y)):
        print("CHARLIE")