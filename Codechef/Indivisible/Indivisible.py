T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    for i in range(1, 100):
        if A % i != 0 and B % i != 0 and C % i != 0:
            print(i)
            break
