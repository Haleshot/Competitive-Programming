from statistics import mode
T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    J = mode(A)
    CN = A.count(J)
    print(N - CN)