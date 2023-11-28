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
    D.clear()
    r = 1
    for i in A:
        p = bisect_left(D, i)
        if p == len(D):
            D.append(i)
        else:
            D[p] = i
        R = max(r, len(D) + S.pop() - 1)
    print(R)    