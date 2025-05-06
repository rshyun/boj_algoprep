def main():

    n = int(input())
    score = list(map(int, input().split()))
    m = max(score)

    return sum(score) / m * 100 / n

if __name__ == '__main__':
    print(main())