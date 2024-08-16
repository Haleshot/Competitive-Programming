T = int(input())
while T:
    T -= 1
    A, B = map(int, input().split())
    A = 7 - A
    B = 7 - B
    print(min(A, B))
