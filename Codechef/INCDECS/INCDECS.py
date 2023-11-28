from bisect import bisect_left

T = int(input())
while T:
    T -= 1
    N = int(input())
    A = list(map(int, input().split()))
    D = []
    S = []
