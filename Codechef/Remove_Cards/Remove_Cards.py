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

    highest_mode = max(freq_dict, key = lambda x : freq_dict[x])
    

