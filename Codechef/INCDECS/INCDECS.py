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
        P = bisect_left(D, i)
        if P == len(D):
            D.append(i)
        else:
            D[P] = i
        S.append(len(D))
    D.clear()
    R = 1
    for i in A:
        P = bisect_left(D, i)
        if P == len(D):
            D.append(i)
        else:
            D[P] = i
        R = max(R, len(D) + S.pop() - 1)
    print(R)
