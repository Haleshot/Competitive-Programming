T = int(input())
while T:
    T -= 1
    Na, Nb, Nc = map(int, input().split())
    
    if Na > (Nb + Nc):
        print("YES")
    
    elif Nb > (Na + Nc):
        print("YES")
    
    elif Nc > (Na + Nb):
        print("YES")

    
    else:
        print("NO")