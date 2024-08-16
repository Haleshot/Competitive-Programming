T = int(input())
while T:
    T -= 1
    N = int(input())
    A = input()
    B = input()
    mp1 = {"1": 0, "0": 0}
    mp2 = {"1": 0, "0": 0}

    for i in A:
        if i in mp1.keys():
            mp1[i] += 1
        else:
            mp1[i] = 1

    for i in B:
        if i in mp2.keys():
            mp2[i] += 1
        else:
            mp2[i] = 1
    if mp1 == mp2:
        print("YES")
    else:
        print("NO")
