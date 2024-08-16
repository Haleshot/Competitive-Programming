T = int(input())
while T:
    T -= 1
    N, X = map(int, input().split())
    salary = 2**X
    if N == 1:
        print(int(salary - 0.5 * salary))
    else:
        salary -= 0.5 * salary
        for i in range(N - 1):
            salary -= 0.5 * salary
        print(int(salary))
