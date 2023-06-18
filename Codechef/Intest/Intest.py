N, K = map(int, input().split())
c = 0
for i in range(N):
    a = int(input())
    if a % K == 0:
        c += 1
print(c)