T = int(input())
while T:
    T -= 1
    A, B, A1, B1, A2, B2 = map(int, input().split())
    l1 = [A1, B1]
    l2 = [A2, B2]

    if A in l1 and B in l1:
        print(1)
    elif A in l2 and B in l2:
        print(2)
    else:
        print(0)
