def main():

    import sys

    n = int(sys.stdin.readline())
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    x = int(sys.stdin.readline())
    total = 0
    left, right = 0, n - 1

    while left < right:
        result = lst[left] + lst[right]
        if result == x:
            total += 1
            left += 1
            right -= 1
        elif result < x:
            left += 1
        elif result > x:
            right -= 1

    return total

if __name__ == '__main__':
    print(main())