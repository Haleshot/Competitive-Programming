N, M = map(int, input().split())
X = [int(input()) for i in range(N)]
X.sort()
i, a = 0, 0
while i < N - 1:
    if X[i + 1] - X[ i ] <= M:
        a += 1
        i += 2 
    else:
        i += 1 
print(a)