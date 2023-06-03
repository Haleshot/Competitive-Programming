T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    print(max(A, B, C) - min(A, B, C))
    