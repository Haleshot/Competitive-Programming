T = int(input())
while T:
    T -= 1
    N, X, Y = map(int, input().split())
    S = input()
    l = [i for i in S]
    if X > Y:
        l.sort()
    else:
        l.sort(reverse=True)
    c1 = 0
    c2 = 0
    for i in range(l):
        if l[i] == 0 and l[i + 1] == 1:
            c1 += 1
        elif l[i] == 1 and l[i + 1] == 0:
            c2 += 1
    
    
