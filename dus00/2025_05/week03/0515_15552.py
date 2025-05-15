import sys

def main():
    input = sys.stdin.readline
    output = sys.stdout.write

    a = int(input())

    for _ in range(a):
        s, t = map(int, input().split())
        output(str(s + t) + '\n')

if __name__ == "__main__":
    main()