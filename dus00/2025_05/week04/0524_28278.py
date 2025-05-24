import sys
def main():
    input = sys.stdin.readline

    n = int(input())
    stack = []

    for _ in range(n):
        command = input().rstrip()
        if command[0] == '1':
            stack.append(int(command[1:]))
        elif command[0] == '2':
            print(stack.pop() if stack else -1)
        elif command[0] == '3':
            print(len(stack))
        elif command[0] == '4':
            print(0 if stack else 1)
        elif command[0] == '5':
            print(stack[-1] if stack else -1)

if __name__ == "__main__":
    main()
