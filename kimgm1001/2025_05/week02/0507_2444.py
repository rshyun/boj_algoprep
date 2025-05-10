def main():

    n = int(input())

    for i in range(1, n + 1):
        print(' '*(n - i) + '*'*(1 + 2*(i-1)))

    for j in range(1, n):
        print(' '*(j) + '*'*(1 + 2*(n-2) - 2*(j-1)))

if __name__ == '__main__':
    print(main())