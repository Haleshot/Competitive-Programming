T = int(input())
while T:
    T -= 1
    N = int(input())
    if N <= 10:
        print("LOWER DOUBLE")
    elif N >= 11 and N <= 15:
        print("LOWER SINGLE")
    elif N >= 16 and N <= 25:
        print("UPPER DOUBLE")
    else:
        print("UPPER SINGLE")
