def main():

    n = int(input())

    for _ in range(n):
        a, b = map(int, input().split())
        m = max(a, b)
        n = min(a, b)
        while m % n != 0:
            q = m // n
            r = m - n * q
            m = n
            n = r
        print(int(a * b / n))

if __name__ == '__main__':
    print(main())