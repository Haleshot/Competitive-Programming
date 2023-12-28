T = int(input())
while T:
    T -= 1
    Xa, Xb, Xc = map(int, input().split())
    if (Xa > 50 and (Xb <= 50 and Xc <= 50)):
        print("A")
    elif (Xb > 50 and (Xa <= 50 and Xc <= 50)):
        print("B")
    elif (Xc > 50 and (Xa <= 50 and Xb <= 50)):
        print("C")
    else:
        print("NOTA")