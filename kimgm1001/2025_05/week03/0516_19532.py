def main():
    a, b, c, d, e, f = map(int, input().split())

    [result] = [[i, j] for i in range(-999, 1000) for j in range(-999, 1000) if a * i + b * j == c and d * i + e * j == f]

    print(*result)

if __name__ == '__main__':
    print(main())