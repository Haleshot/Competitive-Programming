from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, ('0 ' + input()).split()))
for i in range(1, N + 1):
    A[i] += A[i - 1]
ans = []
for _ in range(Q):
    i, x = map(int, input().split())
    j = bisect_left(A, x + A[i - 1])
    if j > N:
        j = -1
    ans.append(j)
print(*ans)