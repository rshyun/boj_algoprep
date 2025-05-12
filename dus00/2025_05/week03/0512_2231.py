def main():
    n = int(input())

    for i in range(1, n + 1):
        s = i
        a = i
        while a:
            s += a % 10
            a //= 10
        if s == n:
            print(i)
            break
    else:
        print(0)

if __name__ == "__main__":
    main()
