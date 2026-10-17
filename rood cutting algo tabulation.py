def rodtab(prince,n):
    dp = [0] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        best = 0
        for j in range(1, i + 1):
            best = max(best, prince[j - 1] + dp[i - j])
        dp[i] = best

    return dp[n]


n = 3
price = [2, 5, 7, 8, 10]
print("Maximum revenue:", rodtab(price, n))