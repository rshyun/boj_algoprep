def main():

    n = int(input())
    length = 2

    for _ in range(n):
        length += length - 1

    return length**2

if __name__ == '__main__':
    print(main())