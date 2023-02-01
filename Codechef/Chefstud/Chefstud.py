T = int(input())
while T:
    T -= 1
    s = input()
    for i in range(len(s) - 1):
        c = 0
        if s[i] == "<" and s[i + 1] == ">":
            c += 1
    print(c)