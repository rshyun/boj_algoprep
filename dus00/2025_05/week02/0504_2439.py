def main():
    a = int(input())
    for i in range(1, a + 1):
        print(" " * (a - i) + "*" * i)

if __name__ == "__main__":
    main()