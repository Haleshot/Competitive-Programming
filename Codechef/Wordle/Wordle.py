T = int(input())
while T:
    T -= 1
    S = input()
    T = input()
    for i in S:
        for j in T:
            if i == j:
                print("G", end = "")
            else:
                print("B", end = "")