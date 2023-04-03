T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    max_D = max(A, B, C)
    for i in range(max_D):
        if (i % A == 0 and i % B == 0 and i % C == 0):
            print(i)