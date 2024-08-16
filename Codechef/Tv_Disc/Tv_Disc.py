T = int(input())
while T:
    T -= 1
    A, B, C, D = map(int, input().split())
    A -= C
    B -= D
    if A < B:
        print("First")
    elif B < A:
        print("Second")
    else:
        print("Any")
