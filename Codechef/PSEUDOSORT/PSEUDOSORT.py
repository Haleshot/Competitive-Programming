T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    A1 = A
    A1.sort()
    if A1 == A:
        print("YES")
    