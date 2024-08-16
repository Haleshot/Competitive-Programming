T = int(input())
while T:
    T -= 1
    A, B = map(int, input().split())
    min_A = 100 - A
    min_B = 200 - (B * 200) / 100
    # print(min_A, "\n" , min_B)
    if min_A < min_B:
        print("FIRST")
    elif min_A > min_B:
        print("SECOND")
    else:
        print("BOTH")
