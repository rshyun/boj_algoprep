def main():

    t = int(input())

    for i in range(t):
        price = int(input())
        for j in [25, 10, 5, 1]:
            print(price // j, end=' ')
            price = price % j
        print()

if __name__ == '__main__':
    print(main())