def main():

    s = [input() for _ in range(5)]
    result = []

    for j in range(15):
        for i in range(5):
            if j < len(s[i]):
                result.append(s[i][j])

    print(''.join(result))

if __name__ == '__main__':
    print(main())