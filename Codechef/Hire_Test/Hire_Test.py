T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    inp = []
    for i in range(N):
        inp.append(input())
    s = ''
    for i in inp:
        if ((i.count("P") >= X or i.count("P") >= (X - 1)) and i.count("F") >= Y):
            s += '1'
        else:
            s += '0'
    print(s)