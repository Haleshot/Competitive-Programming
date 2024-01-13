T = int(input())
while T:
    T -= 1
    N, X, S = map(int, input().split())
    for i in range(S):
        new_x = 0
        A, B = map(int, input().split())
        