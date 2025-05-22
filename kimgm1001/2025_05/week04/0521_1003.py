def main():

    t = int(input())
    max_n = 0
    dp = [(1, 0), (0, 1)]
    lst = []

    for _ in range(t):
        n = int(input())
        lst.append(n)
        max_n = max(n, max_n)

    for i in range(2, max_n + 1):
        dp.append((dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]))

    for j in lst:
        print(*dp[j])

if __name__ == '__main__':
    print(main())