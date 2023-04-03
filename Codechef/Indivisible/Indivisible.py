T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    for i in range(1, 100):
        if (i % A == 1 and i % B == 1 and i % C == 1):
            print(i)