import sys

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    input_chars = list(input())
    bomb_chars = list(input())
    
    str_stack = list()
    for x in input_chars:
        str_stack.append(x)
        
        if (x == bomb_chars[-1]) and (str_stack[-1 * len(bomb_chars):] == bomb_chars):
            for _ in range(len(bomb_chars)):
                str_stack.pop()
    
    print("".join(str_stack) if len(str_stack) != 0 else "FRULA")

if __name__ == "__main__":
    main()
    