T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    inp = []
    for i in range(N):
        ele = input()
        inp.append(ele)
    s = ''
    U_Count, P_Count, F_Count = inp.count("U"), inp.count("P"), inp.count("F")
    if ((F_Count >= X or F_Count >= X - 1) and P_Count >= Y):
        s += '1'
    else:
        s += '0'
    print(s)