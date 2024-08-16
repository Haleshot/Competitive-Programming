N = int(input())
L = list(map(int, input().split()))
for i in range(1, N + 1):
    print(L[N - i], end=" ")
