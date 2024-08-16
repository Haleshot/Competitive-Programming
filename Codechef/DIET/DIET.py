T = int(input())
while T:
    T -= 1
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    c = 0
    for i in range(N):
        total += A[i] - K
        if total < 0:
            c += 1
            break
    if c > 0:
        print("NO", (i + 1))
    else:
        print("YES")
