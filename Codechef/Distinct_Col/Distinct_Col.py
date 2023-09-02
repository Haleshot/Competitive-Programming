T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A))