T = int(input())
while T:
    T -= 1
    A, B, P, Q = map(int, input().split())
    if A == P and B == Q:
        print(0)
    elif (A + B) % 2 == (P + Q) % 2:
        print(2)
    else:
        print(1)
