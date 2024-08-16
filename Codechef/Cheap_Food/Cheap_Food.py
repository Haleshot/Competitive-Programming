T = int(input())
while T:
    T -= 1
    X = int(input())
    ten = 0.1 * X
    print(int(max(ten, 100)))
