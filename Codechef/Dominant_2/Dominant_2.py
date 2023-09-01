T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    L = []
    for i in A:
        ele = A.count(i)
        L.append(ele)
    L.sort(reverse=True)
    if L[0] > L[1]:
        print("YES")
    else:
        print("NO")