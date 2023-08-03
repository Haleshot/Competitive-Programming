T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    s = set(A)
    l = []
    flag = False
    for i in s:
        if (A.count(i) >= 2 and A.count(i) >= 2):
            l.append(i)
    l.sort()
    if (len(l) >= 2):
        print(l[-1] * l[-2])
    else:
        print(-1)