T = int(input())
while T:
    T -= 1
    a, b, c, d = map(int, input().split())
    print(max(a, b) + max(c, d))
