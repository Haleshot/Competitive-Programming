T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    om_count = 0
    addy_count = 0
    om_streak = om_count
    addy_streak = addy_count
    for i in range(N):
        if A[i] != 0:
            om_count += 1
        else:
            om_count = 0
            
        if B[i] != 0:
            addy_count += 1
        else:
            addy_count = 0
        om_streak = max(om_count, om_streak)
        addy_streak = max(addy_count, addy_streak)
        
    if om_streak > addy_streak:
        print("Om")
    elif om_streak < addy_streak:
        print("Addy")
    else:
        print("Draw")