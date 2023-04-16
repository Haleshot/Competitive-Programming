T = int(input())
while T:
    T-= 1
    X = int(input())
    if X % 3 == 0:
        print("NORMAL")
    elif X % 3 == 1:
        print("HIGH")
    else:
        print("SMALL")