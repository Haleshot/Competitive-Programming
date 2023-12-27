T = int(input())
while T:
    T -= 1
    A, B = map(int, input().split())
    c = 0
    for i in range(1, 1000):
        if i % 2 == 1:
            A = A - i
            if(A < 0):
                print("Bob")
                break
        else:
            B = B - i
            if(B < 0):
                print("Limak")
                break
            