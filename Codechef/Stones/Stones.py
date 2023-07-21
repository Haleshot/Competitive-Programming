T = int(input())
while T:
    T -= 1
    J = input()
    S = input()
    c = [i for i in J if i in S]
    print([*set(c)])
    # print(len([*set(c)]))