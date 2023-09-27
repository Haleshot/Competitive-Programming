def check_palindrome(seq):
    return seq == seq[::-1]

def min_pal_seq(N, sequence):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        for j in range(i):
            if check_palindrome(sequence[j:i]):
                dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[N]

N = int(input())
sequence = list(map(int, input().split()))

result = min_pal_seq(N, sequence)
print(result)