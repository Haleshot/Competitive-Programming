T = int(input())
while(T):
    T -= 1
    X = int(input())
    X = X + 1
    X = str(X)
    s = len(set(X))
    l = len(X)
    while(s != l):
        X = int(X) + 1
        X = str(X)
        s = len(set(X))
        l = len(X)
    print(int(X))