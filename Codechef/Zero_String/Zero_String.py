T = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    l = [i for i in S]
    c1 = l.count("1")
    c2 = N - c1
    if c1 == N:
        print(1)
    else:
        if c1 > c2:
            print(c1 + 1)
        else:
            print(c1)