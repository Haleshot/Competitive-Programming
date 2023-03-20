T = int(input())
while T:
    T -= 1
    X, A, B = map(int, input().split())
    if (A + (B * 2) >= X):
        print("Qualify")
    else:
        print("NotQualify")