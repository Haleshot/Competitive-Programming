T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N - 1):
        if(A[i + 1] < A[i]):
            A[i + 1], A[i] = A[i], A[i + 1]
            break
    if (sorted(A) == A):
        print("YES")
    else:
        print("NO")