def GCD(input1:int, input2:int) -> int:
    if input1 % input2 == 0:
        return input2
    return GCD(input2, input1%input2)


def main():
    A, B =map(int, input().split())
    print(A * B // GCD(A, B))


if __name__ == "__main__":
    main()
