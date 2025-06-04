from collections import deque
def main():
    n, k = map(int, input().split())

    people = deque(range(1, n + 1))
    result = []

    while people:
        people.rotate(-(k - 1))
        result.append(people.popleft())

    print('<' + ', '.join(map(str, result)) + '>')

if __name__ == '__main__':
    main()