T = int(input())
while T:
    T -= 1
    N = int(input())
    B = input()
    c = B.count('1')
    if(c % 2 == 0):
        print("YES")
    else:
        print("NO")