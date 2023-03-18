T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if X <= Y:
        print(Z)
    else:
        while True:
            Y *= 2
            Z *= 2
            if X <= Y:
                print(Z)
                break