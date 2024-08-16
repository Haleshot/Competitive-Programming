N = int(input())
L = list(map(int, input().split()))
res = [0 for i in range(N)]
res[0] = L[0]
res[1] = L[0] + L[1]
res[2] = max(L[0] + L[2], L[1] + L[2], L[0] + L[1])
for i in range(3, N):
    res[i] = max(L[i] + L[i - 1] + res[i - 3], L[i] + res[i - 2], res[i - 1])
print(max(res))
