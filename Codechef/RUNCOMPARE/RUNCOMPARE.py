T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0 
    for i in range(n):
        if A[i] <= 2 * B[i] and B[i] <= 2 * A[i]:
            ans += 1 
    print(ans)