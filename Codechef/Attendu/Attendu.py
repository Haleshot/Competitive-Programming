T = int(input())
while T:
    T -= 1
    N = int(input())
    B = input()
    remain = 120 - N
    atten_perc = (remain/120) * 100
    if atten_perc >= 75:
        print("YES")
    else:
        print("NO")
    