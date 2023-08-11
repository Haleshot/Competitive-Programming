T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    c = 0
    if (X == 1 and Y == 1 and Z == 1):
        print(3)
    
    elif (X == 0 and Y == 0 and Z == 0):
        print(0)

    else:
        X_remain = X - 1
        Y_remain = Y - 1
        Z_remain = Z - 1
        