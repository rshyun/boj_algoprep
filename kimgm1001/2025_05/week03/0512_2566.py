def main():
    dif = 100
    row = 0

    for i in range(9):
        lst = list(map(int, input().split()))
        row += 1
        for j in lst:
            if 100 - j <= dif:
                dif = 100 - j
                max_value = j
                row_result = row
                col_result = lst.index(j) + 1

    print(max_value)
    print(row_result, col_result)

if __name__ == '__main__':
    print(main())