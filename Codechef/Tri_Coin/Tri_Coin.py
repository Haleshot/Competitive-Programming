T = int(input())
while T:
    T -= 1
    N = int(input())
    max_height = 0

    while N >= max_height + 1:
        max_height += 1
        N -= max_height

    print(max_height)
