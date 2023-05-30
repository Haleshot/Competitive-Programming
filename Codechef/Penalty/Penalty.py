T = int(input())
while T:
    T -= 1
    A = list(map(int, input().split()))
    odd = [A[i] for i in range(len(A)) if (i % 2 == 1)]
    even = [A[i] for i in range(len(A)) if (i % 2 == 0)]
    odd_one_count = [i for i in odd if i == 1]
    even_one_count = [i for i in even if i == 1]
    if (odd_one_count > even_one_count):
        print(2)
    elif (odd_one_count < even_one_count):
        print(1)
    else:
        print(0)