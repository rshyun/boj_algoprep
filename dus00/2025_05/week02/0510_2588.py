def main():
    a = int(input())
    b = input()

    for i in range(3, 0, -1):
        print(a * int(b[i-1]))

    print(a * int(b))

if __name__ == "__main__":
    main()