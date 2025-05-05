def main():

    n = int(input())
    result = 0

    for i in range(n):
        a = input()
        sum = 0
        for i in range(len(a)-1):
            if a[i] != a[i + 1]:
                sum += 1
        if (sum + 1) == len(set(a)):
            result += 1

    return result

if __name__ == '__main__':
    print(main())