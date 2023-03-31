T = int(input())
while T:
    T -= 1
    A, B, C = map(int, input().split())
    if (A > B and A > C):
        print("Alice")
    elif (B > A and B > C):
        print("Bob")
    else:
        print("Charlie")