T = int(input())
while T:
    T -= 1
    X = input()
    Y = input()
    L = len(X)
    c = 0
    for i in range(L):
        if X[i] != "?" and Y[i] != "?":
            if X[i] != Y[i]:
                c += 1
    if c:
        print("No")
    else:
        print("Yes")
