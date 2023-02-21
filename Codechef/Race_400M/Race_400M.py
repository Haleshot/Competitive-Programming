T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if (X//400) > ((Y//400) and (Z//400)):
        print("ALICE")

    elif (Y//400) > ((X//400) and (Z//400)):
        print("BOB")

    elif (Z//400) > ((X//400) and (Y//400)):
        print("CHARLIE")