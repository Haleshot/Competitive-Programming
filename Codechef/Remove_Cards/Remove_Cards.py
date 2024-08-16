T = int(input())
while T:
    T -= 1
    N = int(input())
    l = list(map(int, input().split()))

    freq_dict = {}
    for i in range(len(l)):
        if l[i] in freq_dict.keys():
            freq_dict[l[i]] += 1
        else:
            freq_dict[l[i]] = 1

    highest_mode_number = max(freq_dict, key=lambda x: freq_dict[x])
    c = 0
    for i in l:
        if i != highest_mode_number:
            c += 1

    print(c)
