def rodmemo(price, n, memo):
    if n == 0:
        return 0
    if memo[n] != -1:
        return memo[n]

    best = 0
    for i in range(1, n + 1):
        best = max(best, price[i - 1] + rodmemo(price, n - i, memo))

    memo[n] = best
    return best


n = 4
price = [1,5,8,9]
memo = [-1] * (n + 1)

print("Maximum revenue:", rodmemo(price, n, memo))
