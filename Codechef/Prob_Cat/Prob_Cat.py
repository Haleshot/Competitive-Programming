T = int(input())
while T:
    T -= 1
    X = int(input())
    if X >= 1 and X < 100:
        print("Easy")
    elif X >= 100 and X < 200:
        print("Medium")
    elif X >= 200 and X <= 300:
        print("Hard")
