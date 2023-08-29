T = int(input())
while T:
    T -= 1
    N = int(input())
    L = []
    for i in range(N):
        ele = int(input())
        L.append(ele)
    for i in L:
        if L.count(i) % 2 == 1:
            print(i)
            break