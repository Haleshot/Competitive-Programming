T = int(input())
while T:
    T -= 1
    S1 = input()
    S2 = input()
    N, M = 0, 0
    for j in range(len(S1)):
        if (S1[j] =='?' or S2[j] =='?'):
            N += 1
        elif (S1[j] != S2[j]):
            M += 1
    print(M, (M + N))