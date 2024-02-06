T = int(input())
while T:
    T -= 1
    N = int(input())
    S = list(input())
    R = list(input())
    if ((S.count(1) == R.count(1)) and (S.count(1) == R.count(1))):
        print("YES")
    else:
        print("NO")