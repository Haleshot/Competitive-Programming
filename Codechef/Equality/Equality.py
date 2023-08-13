T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A) // (N - 1)
    for i in A:
        print(S - i, end = " ")
    print()