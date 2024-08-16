T = int(input())
while T:
    T -= 1
    N = int(input())
    l = list(map(str, input().split()))
    A = l.count("A")
    B = l.count("B")
    AB = l.count("AB")
    O = l.count("O")
    if A >= B:
        print(A + AB + O)
    else:
        print(B + AB + O)
