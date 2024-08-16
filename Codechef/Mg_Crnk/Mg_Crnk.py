T = int(input())
while T:
    T -= 1
    n = int(input())
    temp = [list(map(int, input().split())) for _ in range(n)]
    m = 0
    temp[0] = [m := m + temp[0][j] for j in range(n)]
    for i in range(1, n):
        temp[i][0] += temp[i - 1][0]
    for i in range(1, n):
        for j in range(1, n):
            temp[i][j] += max(temp[i - 1][j], temp[i][j - 1])
    print(temp[n - 1][n - 1] / (2 * n - 3) if temp[n - 1][n - 1] >= 0 else "Bad Judges")
