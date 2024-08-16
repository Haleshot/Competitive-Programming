T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    if X % N == 0:
        print("YES")
    else:
        print("NO")
