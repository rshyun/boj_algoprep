def main():
    n = int(input())
    li = []

    for i in range(0, n):
        a = input()
        li.append(a)

    set_li = set(li)
    li = list(set_li)

    li.sort()
    li.sort(key=len)

    for a in li:
        print(a)


if __name__ == "__main__":
    main()