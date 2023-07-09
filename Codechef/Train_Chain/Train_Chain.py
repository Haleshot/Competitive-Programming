T = int(input())
while T:
    T -= 1
    N = int(input())
    B = list(map(str, input().split()))
    A = B.count("A")
    B = B.count("B")
    AB = B.count("AB")
    O = B.count("O")
    if (A >= B):
        print(A + AB + O)
    else:
        print(B + AB + O)