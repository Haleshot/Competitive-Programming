from bisect import bisect_left

T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    D = []
    S = []
    B = reversed(A)
    for i in B:
        p = bisect_left(D ,i)
        if p == len(D):
            D.append(i)
        else:
            D[p] = i
        S.append(len(D))
