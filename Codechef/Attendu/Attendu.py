T = int(input())
while T:
    T -= 1
    N = int(input())
    B = input()
    c1 = 0
    c2 = 0
    for i in B:
        if i == "0":
            c1 += 1
        elif i == "1":
            c2 += 1
    