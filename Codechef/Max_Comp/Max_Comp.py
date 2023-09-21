T = int(input())
while T:
    T -= 1
    N = int(input())
    V = [[0 for i in range(49)] for j in range(49)]
    max_list = [0]*49
    for i in range(N):
        S, E, C = list(map(int, input().split()))
        