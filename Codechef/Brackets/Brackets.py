T = int(input())
while T:
    T -= 1
    A = input()
    balance = 0
    max_balance = 0
    for i in range(len(A)):
        if A[i] == "(":
            balance += 1
        if A[i] == ")":
            balance -= 1

        max_balance = max(max_balance, balance)
    print("(" * max_balance + ")" * max_balance)
