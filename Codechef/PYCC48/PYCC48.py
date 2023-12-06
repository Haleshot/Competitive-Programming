T = int(input())
while T:
    T -= 1
    X, Y = map(int, input().split())
    ans1 = (500 - (X * 2)) + (1000 - ((X + Y) * 4))
    ans2 = (500 - (X + Y) * 2) + 1000 - (Y * 4)    
    A = max(ans1, ans2)
    print(A)