T = int(input())
while T:
    T -= 1
    X = int(input())
    if X > 65:
        print("OVERLOAD")
    elif X < 35:
        print("UNDERLOAD")
    else:
        print("NORMAL")