T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    if (N % X == 0):
        print("YES")
    elif ((N % 2 == 0 and X % 2 == 0) or (X % 2 == 1)):
        print("YES")
    else:
        print("NO")