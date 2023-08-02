T = int(input())
while T:
    T -= 1
    N, A, B = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())