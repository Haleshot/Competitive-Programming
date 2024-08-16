T = int(input())
while T:
    T -= 1
    N = int(input())
    res1 = list(map(int, str(N)))
    res2 = list(map(int, str(N + 1)))
    s1 = sum(res1)
    s2 = sum(res2)
    if (s1 % 2 == 0 and s2 % 2 == 0) or (s1 % 2 == 1 and s2 % 2 == 1):
        print(N + 2)
    else:
        print(N + 1)
