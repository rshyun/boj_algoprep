def main():

    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    dif = m
    for i in num:
        for j in num:
            for k in num:
                if i < j < k:
                    total = i + j + k
                    if dif >= m - total >= 0:
                        dif = m - total
                        result = total

    return result

if __name__ == '__main__':
    print(main())