def main():

    x = int(input())
    n = 0

    while x > 0:
        n += 1
        x -= n

    x = x + n
    if (n + 1) % 2 == 0:
        print(f'{n + 1 - x}/{x}')
    else:
        print(f'{x}/{n + 1 - x}')

if __name__ == '__main__':
    main()