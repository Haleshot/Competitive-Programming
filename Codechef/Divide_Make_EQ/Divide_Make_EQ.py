from math import gcd
T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    if gcd(*A) != min(A):
        print(len(A))
    else:
        print(len(A) - A.count(min(A)))