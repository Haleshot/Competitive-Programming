T = int(input())
while T:
    T -= 1
    L, R = map(input().split())    
    L = 2 * L
    R = 2 * R
    
    print(R - L + 1)