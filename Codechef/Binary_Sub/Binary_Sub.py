T = int(input())
while T:
    T -= 1
    S = input() 
    N = len(S)
    M = 998244353
    dp = [0] * N
    dp[0] = 1 
    if(N == 1):
        print(dp[0])
    else:
        if(S[0] == S[1]):
            dp[1] = 1 
        else:
            dp[1] = 2   
        for i in range(2, N):
            if(S[i] == S[i - 1]):
                dp[i] = (dp[i - 1]) % M 
            else:
                dp[i] = (dp[i - 1] + dp[i - 2]) % M      
        print(dp[N - 1]) 