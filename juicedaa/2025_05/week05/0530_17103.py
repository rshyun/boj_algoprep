def main():
    import sys

    t = int(sys.stdin.readline())
    primes = [True] * 1000001
    primes[0] = primes[1] = False
    for i in range(2, int(1000001 ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, 1000001, i):
                primes[j] = False

    real_p = {i for i, v in enumerate(primes) if v}

    for _ in range(t):
        n = int(sys.stdin.readline())
        cnt = 0
        for i in range(2, n // 2 + 1):
            if i in real_p:
                if (n - i) in real_p:
                    cnt += 1
        print(cnt)

if __name__ == "__main__":
    main()