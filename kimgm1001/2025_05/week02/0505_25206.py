def main():
    score1 = 0
    score2 = 0

    for i in range(20):
        a, b, c = map(str, input().split())
        if c == 'A+':
            c = 4.5
        elif c == 'A0':
            c = 4.0
        elif c == 'B+':
            c = 3.5
        elif c == 'B0':
            c = 3.0
        elif c == 'C+':
            c = 2.5
        elif c == 'C0':
            c = 2.0
        elif c == 'D+':
            c = 1.5
        elif c == 'D0':
            c = 1.0
        elif c == 'F':
            c = 0.0
        else:
            continue

        if isinstance(c, float):
            score1 += float(b) * c

        score2 += float(b)

    return score1 / score2

if __name__ == '__main__':
    print(main())