T = int(input())
while T:
    T -= 1
    N = int(input())
    L = list(map(int, input().split()))
    print(len(set(L)))
