T = int(input())
while T:
    T -= 1
    A, B = map(int, input().split())
    print(min(A, B))
