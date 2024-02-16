for _ in range(int(input())):
    N = int(input())
    S = list(input())
    z_c = S.count("0")
    o_c = S.count("1")
    
    if o_c == z_c:
        print(N)
    else:
        res = min(o_c, z_c) * 2 + 1
        print(res)