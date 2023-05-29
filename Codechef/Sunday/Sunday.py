T = int(input())
while T:
    T -= 1
    N = int(input())
    A = input()
    B = A.split()
    for i in range(len(B)):
        B[i] = int(B[i])
    weekend = [6, 7, 13, 14, 20, 21, 27, 28]
    matching = [i for i in B if i in weekend]
    print()
    print((len(B) - len(matching)) + 8)
    print()