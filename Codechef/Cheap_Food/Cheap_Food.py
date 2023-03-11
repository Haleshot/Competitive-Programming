T = int(input())
while T:
    T -= 1
    X = int(input())
    ten = X - 0.1 * X
    hund = X - 100
    print(min(ten, hund))