T = int(input())
while T:
    T -= 1 
    X, Y = map(int, input().split())
    if Y >= X and Y <= (X + 200):
        print("YES")

    else:
        print("NO")