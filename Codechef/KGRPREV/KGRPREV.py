T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    res = []
    for i in range(0, N, M):
        temp = arr[i : i + M]
        res += temp[::-1]
    print(*res)
