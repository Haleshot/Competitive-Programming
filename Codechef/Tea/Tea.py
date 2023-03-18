T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if X <= Y:
        print(Z)
    else:
        i = 2
        while True:
            temp_Y = Y * i
            temp_Z = Z * 2
            if X <= Y:
                print(Z)
                break