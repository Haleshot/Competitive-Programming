T = int(input())
while T:
    T -= 1
    X = int(input())
    if (X <= 3):
        print("BRONZE")
    elif (X > 3 and X <= 6):
        print("SILVER")
    else:
        print("GOLD")