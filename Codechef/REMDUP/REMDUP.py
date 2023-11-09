T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))[:N]
    B = set(A)
    B = list(B)
    B.sort()
    print(*B)   