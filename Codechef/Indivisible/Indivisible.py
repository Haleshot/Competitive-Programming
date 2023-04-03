T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    min_num = min(A, B, C)
    for i in range(min_num, 100):
        if (A % i != 0 and B % i != 0 and C % i != 0):
            print(i)