T = int(input())
while T:
    T -= 1
    A, B, A1, B1, A2, B2 = map(int, input().split())
    if A in [A1, B1] and B in [A1, B1]:
        print(1)
    elif A in [A2, B2] and B in [A2, B2]:
        print(2)
    else:
        print(0)