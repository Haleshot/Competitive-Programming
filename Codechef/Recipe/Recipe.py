def gcd_calc(a, b):
    while b:
        a, b = b, a % b
    return a

T = int(input())
while T:
    T -= 1
    N = list(map(int(input())))
    
