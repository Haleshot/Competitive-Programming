from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, ('0 ' + input()).split()))

for i in range(1, N + 1):
    A[i] += A[i - 1]
