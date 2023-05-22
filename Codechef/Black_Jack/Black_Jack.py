T = int(input())
while T:
    T -= 1
    A, B = map(int, input().split())
    C = 21 - (A + B)
    if C <= 10:
        print(C)
    else:
        print(-1)