def main():

    import sys

    n = int(sys.stdin.readline())
    s = []

    for _ in range(n):
        x = sys.stdin.readline().split()

        if x[0] == '1':
            s.append(x[1])

        if x[0] == '2':
            if s:
                print(s[-1])
                s.pop()
            else:
                print(-1)

        if x[0] == '3':
            print(len(s))

        if x[0] == '4':
            print(0 if s else 1)

        if x[0] == '5':
            print(s[-1] if s else -1)

if __name__ == '__main__':
    main()