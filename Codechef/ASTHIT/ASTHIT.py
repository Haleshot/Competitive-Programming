T = int(input())
while T:
    T -= 1
    n = int(input())
    dir = []
    pow = [] 
    for i in range(n):
        ele1, ele2 = list(map(int, input().split()))
        dir.append(ele1)
        pow.append(ele2)
        
    stack = []
    a = []
    for i in range(n):
        if dir[i] == 1:
            stack.append(i)
        else:
            while stack and pow[i] > pow[stack[-1]]:
                pow[i] += pow[stack[-1]]
                stack.pop()
 
            if stack:
                if pow[i] == pow[stack[-1]]:
                    stack.pop()
                else:
                    pow[stack[-1]] += pow[i]
            else:
                a.append(i)         
    while stack:
        a.append(stack.pop())
    a.sort()
    print(len(a))
    if len(a) > 0:
        for i in a:
            print(i + 1, end = " ")