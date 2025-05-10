def main():

    m = int(input())
    n = int(input())
    lst = []

    for i in range(m, n + 1):
        lst.append(i)
        if 1 in lst:
            lst.remove(1)
        for j in range(2, i):
            if i % j == 0:
                lst.remove(i)
                break
            else:
                continue

    if len(lst) != 0:
        print(sum(lst))
        print(min(lst))
    else:
        print(-1)

if __name__ == '__main__':
    print(main())