T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    if ((2 * X) > (5 * Y)):
        print("Chocolate")
    elif((2 * X) < (5 * Y)):
        print("Candy")
    else:
        print("Either")