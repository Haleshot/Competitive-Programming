T = int(input())
while T:
    T -= 1
    N = int(input())
    A = input()
    
    weekend = [6, 7, 13, 14, 20, 21, 27, 28]
    matching = [i for i in A if i in weekend]
    print(30 - (A - matching) - 8)