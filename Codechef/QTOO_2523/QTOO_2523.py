T = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    S1 = set(S)
    if len(S1) == len(S):
        print(-1)
    else:
        print(len(S) - 2)