def main():

    import sys

    n = int(sys.stdin.readline().rstrip())
    lst = []

    for i in range(n):
        lst.append(int(sys.stdin.readline().rstrip()))

    lst.sort()

    for j in lst:
        print(j)

if __name__ == '__main__':
    print(main())