T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N - X] - 1)
