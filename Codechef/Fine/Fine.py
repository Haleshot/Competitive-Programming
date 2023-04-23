T = int(input())
while T:
    T -= 1
    X = int(input())
    if (X > 70 and X <= 100):
        print("500")
    elif (X >= 100):
        print("2000")
    else:
        print("0")