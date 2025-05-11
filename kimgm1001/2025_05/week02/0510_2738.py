def main():

        n, m = map(int, input().split())
        lst1 = []
        lst2 = []

        for i in range(n):
            a = list(map(int, input().split()))
            lst1 += a

        for j in range(n):
            b = list(map(int, input().split()))
            lst2 += b

        for k in range(len(lst1)):
            lst1[k] += lst2[k]

        while len(lst1) != 0:
            print(*lst1[0:m])
            lst1 = lst1[m:]

if __name__ == '__main__':
    print(main())