T = int(input())
while T:
    T -= 1
    N, X, Y = map(int, input().split())
    S = input()
    l = [i for i in S]
    if X < Y:
        l.sort()
    else:
        l.sort(reverse=True)  # Sorting by 1
    c1 = 0
    c2 = 0
    for i in range(len(l) - 1):
        if l[i] == "0" and l[i + 1] == "1":
            c1 += 1
        elif l[i] == "1" and l[i + 1] == "0":
            c2 += 1
    print(c1, ",", c2)
    print((X * c1) + (Y * c2))
