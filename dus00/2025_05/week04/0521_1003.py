dp = {}

def fibonacci_count(n):
    if n in dp:
        return dp[n]

    if n == 0:
        dp[n] = (1, 0)
    elif n == 1:
        dp[n] = (0, 1)
    else:
        count1 = fibonacci_count(n - 1)
        count2 = fibonacci_count(n - 2)
        dp[n] = (count1[0] + count2[0], count1[1] + count2[1])
    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    result = fibonacci_count(n)
    print(result[0], result[1])

if __name__ == "__main__":
    fibonacci_count(n)