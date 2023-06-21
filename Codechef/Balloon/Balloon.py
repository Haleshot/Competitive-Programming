T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    c = 0
    for i in range(N):
        if A[i] <= 7:
            c += 1
        if c == 7:
            print(i + 1)
            break