def main():
    n = int(input())
    lst = list(map(int, input().split()))
    lmax = max(lst)
    stsum = sum(lst)

    return stsum * 100 / lmax / n

if __name__ == "__main__":
    print(main())