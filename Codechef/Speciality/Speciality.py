T = int(input())
while T:
    T -= 1
    X, Y, Z = map(int, input().split())
    if X > Y:
        if X > Z:
            print("Setter")
        else:
            print("Editorialist")
    else:
        if Y > Z:
            print("Tester")
        else:
            print("Editorialist")
