for _ in range(int(input())):
    N = int(input())
    S = list(input())
    z_c = S.count("0")
    o_c = S.count("1")
    if z_c == 1 or o_c == 1:
        print(1)
    else:
        d = [] * 100
        s = 2
        for i in range(2, 100):
            d[i] = [S]
            s += 2
        print(d)