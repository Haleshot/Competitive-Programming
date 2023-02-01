T = int(input())
while T:
    T -= 1
    s = input()
    for i in s:
        c = 0
        if i == "<" and i + 1 == ">":
            c += 1
    print(c)