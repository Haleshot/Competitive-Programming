T = int(input())
while T:
    T -= 1
    S = input()
    vowels = "aeiou"
    length = len(S)
    c = 0
    for i in range(length - 2):
        if S[i] in vowels and S[i+1] in vowels and S[i+2] in vowels:
            c = 1
    if (c == 1):
        print("Happy")
    else:
        print("Sad")