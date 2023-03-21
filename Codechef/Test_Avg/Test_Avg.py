import math
T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    if (((A + B)/2 >= 35) or ((A + C)/2 >= 35) or ((B + C)/2 >= 35)):
        print("PASS")
    else:
        print("FAIL")