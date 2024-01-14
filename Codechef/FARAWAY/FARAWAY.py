T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    summation, maximum = 0, 0
    for i in range(N):
        if A[i] > M // 2:
            maximum = abs(A[i] - 1)
        else:
            maximum = abs(A[i] - M)
        summation = summation + maximum
        maximum = 0
    print(summation)