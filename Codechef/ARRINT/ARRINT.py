T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    A1 = set(map(int, input().split()))
    B1 = set(map(int, input().split()))
    C1 = set(map(int, input().split()))
    A1 = A1.intersection(B1)
    A1 = A1.intersection(C1)
    print(len(A1))
