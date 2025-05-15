def main():

    n = int(input())
    i = max(0, n-53)

    while i + sum(map(int, str(i))) != n and i < n:
        i += 1

    if i != n:
        return i
    else:
        return 0

if __name__ == '__main___':
    print(main())