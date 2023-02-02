T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))

    d = {}
    c = 0
    for i in range(len(A)):
        if A[i] in d.keys():
            d[A[i]] += 1
        else:
            d[A[i]] = 1

    print(d.values())