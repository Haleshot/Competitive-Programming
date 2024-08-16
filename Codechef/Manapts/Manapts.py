T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    print(Y // X)  # Prints the output by taking int value of Y/X
