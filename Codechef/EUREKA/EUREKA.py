def calc(n):
    return round(((0.143 * n)**n))

T = int(input())
while T:
    T -= 1
    N = int(input())
    print(calc(N))