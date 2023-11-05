T = int(input())
while T:
    T -= 1
    X = int(input())
    X = x + 1
    X = str(x)
    s = len(set(x))
    l = len(x)
    while(s != l):
        x = int(x) + 1
        x = str(x)
        s = len(set(x))
        l = len(x)
    print(int(x))