T = int(input())
while T:
    T -= 1
    N = int(input())
    l = list(map(int, input().split()))
    num = [i for i in l if i >= 1000]
    print(len(num))
