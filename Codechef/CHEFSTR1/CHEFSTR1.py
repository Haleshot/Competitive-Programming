T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    c = 0
    for i in range(N - 1):
        c += abs(A[i + 1] - A[i]) - 1
    print(c)
