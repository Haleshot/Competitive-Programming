T = int(input())
while T:
    T -= 1
    N = int(input())
    Na, Nb, Nc, Nd = map(int, input().split())
    print(max(Na, Nb, Nc, Nd))