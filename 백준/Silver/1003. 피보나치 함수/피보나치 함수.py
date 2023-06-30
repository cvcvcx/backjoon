def fibonacci(n):
    if dp[n] == -1:
        dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]


n = int(input())
dp = [-1] * 41
dp[0] = 0
dp[1] = 1
for _ in range(n):
    m = int(input())
    if m == 0:
        print(1, 0)
    elif m == 1:
        print(0, 1)
    else:
        print(fibonacci(m-1), fibonacci(m))
