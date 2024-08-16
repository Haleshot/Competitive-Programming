T = int(input())
while T:
    T -= 1
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    first, second = 0, 0
    for i in range(1, N + 1):
        if i in A and i in B:
            first += 1
        elif i not in A and i not in B:
            second += 1

    print(str(first), " ", str(second))
