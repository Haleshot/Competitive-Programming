T = int(input())
while T:
    T -= 1
    N, X, S = map(int, input().split())
    new_x = X
    for i in range(S):
        A, B = map(int, input().split())
        if new_x == A:
            new_x = B
        elif new_x == B:
            new_x = A
    print(new_x)