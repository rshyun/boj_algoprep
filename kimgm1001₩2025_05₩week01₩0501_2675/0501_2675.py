def main():
    t = int(input())
    for i in range(t):
        r, s = map(str, input().split())
        for j in range(0, len(s)):
            print(s[j]*int(r), end="")
        print()

if __name__ == '__main__':
    main()