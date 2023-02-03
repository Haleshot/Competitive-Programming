T = int(input())
while T:
    T -= 1
    N = int(input())
    B = input()
    c1 = 0
    for i in B:
        if i == "1":
            c1 += 1
    remain = 120 - N + c1
    atten_perc = (remain/120) * 100
    if atten_perc >= 75:
        print("YES")
    else:
        print("NO")