T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = list(map(int, input().split()))
    for i in range(M):
        if B[i] in A:
            print("Yes", end=" ")
        else:
            print("No", end=" ")
    print()
