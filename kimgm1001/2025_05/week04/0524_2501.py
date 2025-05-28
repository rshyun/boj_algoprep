def main():

    n, k = map(int, input().split())
    a = 0
    lst = []

    while a <= n:
        a += 1
        if n % a == 0:
            lst.append(a)

    if len(lst) >= k:
        print(lst[k-1])
    else:
        print(0)

if __name__ == '__main__':
    main()