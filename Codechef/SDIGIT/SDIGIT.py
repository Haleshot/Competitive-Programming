T = int(input())
while T:
    T -= 1
    D, N = map(int, input().split())
    A = input().split()
    ans = []
    if D == 1:
        ans = A[0] * N
    else:
        while N:
            if A[0] != "0" or not ans:
                N -= 1
            N, i = divmod(N, D)
            ans.insert(0, A[i])
    print("".join(ans))
