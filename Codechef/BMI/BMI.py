T = int(input())
while T:
    T -= 1
    M, H = map(int, input().split())
    result = M / H**2
    if result <= 18:
        print(1)
    elif result >= 19 and result <= 24:
        print(2)
    elif result >= 25 and result <= 29:
        print(3)
    else:
        print(4)
