T = int(input())
while T:
    T -= 1
    N = int(input())
    count = 0 
    while N % 2 == 0:
        N = N//2
        count += 1 
    print(1 - (count % 2))