T = int(input())
while T:
    T -= 1
    L = list(map(int,input().split()))
    max_L = max(L)
    L.remove(max_L)
    if max_L == sum(L):
        print("Yes")
    else:
        print("No")