def main():
    start = int(input())
    end = int(input())

    primes = [n for n in range(start, end + 1) if n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]

    if primes:
        print(sum(primes))
        print(min(primes))
    else:
        print(-1)

if __name__ == "__main__":
    main()
