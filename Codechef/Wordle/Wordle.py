Test = int(input())
while Test:
    Test -= 1
    print()
    S = input()
    T = input()
    for i in range(5):
        if S[i] == T[i]:
            print("G", end = '')
        else:
            print("B", end = '')