T = int(input())
while T:
    T -= 1
    A, B, X = map(int, input().split())
    if(((A - B) / 2) % X == 0):
        print("YES")
    else:
        print("NO")