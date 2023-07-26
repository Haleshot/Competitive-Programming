T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    inp = []
    for i in range(N):
        ele = input()
        inp.append(ele)
    U_Count, P_Count, F_Count = 0, 0, 0