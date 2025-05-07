def main():
    num = int(input())
    bun = 1

    while num > bun:
        num -= bun
        bun += 1

    if bun % 2 == 0:
        a = num
        b = bun - num + 1
    elif bun % 2 == 1:
        a = bun - num + 1
        b = num

    print(f"{a}/{b}")

if __name__ == "__main__":
    main()