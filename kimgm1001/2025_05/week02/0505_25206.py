def main():
    score1 = 0
    score2 = 0

    for _ in range(20):
        a, b, c = map(str, input().split())
        b = float(b)

        if c == 'P':
            continue

        if c == 'A+':
            grade = 4.5
        elif c == 'A0':
            grade = 4.0
        elif c == 'B+':
            grade = 3.5
        elif c == 'B0':
            grade = 3.0
        elif c == 'C+':
            grade = 2.5
        elif c == 'C0':
            grade = 2.0
        elif c == 'D+':
            grade = 1.5
        elif c == 'D0':
            grade = 1.0
        elif c == 'F':
            grade = 0.0
        else:
            continue

        score1 += b * grade
        score2 += b

    return score1 / score2

if __name__ == '__main__':
    print(main())
