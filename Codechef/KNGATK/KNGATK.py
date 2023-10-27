T = int(input())
while T:
    T -= 1
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    print(A[1])