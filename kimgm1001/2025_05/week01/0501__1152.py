def main():
    a = input()
    b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = len(a)
    for i in range(0, len(a)):
        if a[i] in b:
            sum -= 1
    if a[0] not in b:
        sum -= 1
    if a[-1] not in b:
        sum -= 1
    print(sum + 1)

if __name__ == __main__:
    main()