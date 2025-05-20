import sys
input = sys.stdin.readline

def main():
    MAX_N = 10

    dp = [0] * (MAX_N + 1)
    dp[0] = 1

    for i in range(1, MAX_N + 1):
        if i - 1 >= 0: dp[i] += dp[i - 1]
        if i - 2 >= 0: dp[i] += dp[i - 2]
        if i - 3 >= 0: dp[i] += dp[i - 3]

    t = int(input())

    for _ in range(t):
        n = int(input())
        print(dp[n])

if __name__ == "__main__":
    main()