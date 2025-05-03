def main():

    S = input()

    s = S.lower()
    result = {}

    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    sum = 0
    for j in list(result.values()):
        if j == max(result.values()):
            sum += 1

    if sum == 1:
        for k in result:
            if result[k] == max(result.values()):
                print(k.upper())
    else:
        print('?')

if __name__ == '__main__':
    print(main())