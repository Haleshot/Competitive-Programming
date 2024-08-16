T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    c = 0
    for i in range(N - 1):
        j = i + 1
        if A[j] - A[i] > 1:
            c += 1
    if c > 0:
        print("NO")
    else:
        print("YES")
