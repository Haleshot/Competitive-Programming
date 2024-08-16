T = int(input())
while T:
    T -= 1
    S = input()
    L = list(S)
    c = 0
    L1 = S.count("xy")
    L3 = S.replace("xy", "")
    L2 = L3.count("yx")
    print(L1 + L2)
