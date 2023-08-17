N = int(input())
while N:
    N -= 1
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])