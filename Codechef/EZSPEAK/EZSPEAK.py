T = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    c = 0
    ans = False
    for i in str(S):
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            c += 1
        else:
            c = 0
        if c >= 4:
            ans = True
    if ans == False:
        print("YES")
    else:
        print("NO")
