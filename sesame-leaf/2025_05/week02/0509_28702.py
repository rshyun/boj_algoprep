import sys

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    num_count = 0
    input_num = 0
    for i in range(3):
        
        input_str = input()
        
        try:
            input_num = int(input_str)
            num_count = i + 1
        except:
            pass
    
    if (input_num + 4 - num_count) % 3 == 0:
        print("Fizz", end="")
    
    if (input_num + 4 - num_count) % 5 == 0:
        print("Buzz", end="")
    
    if (input_num + 4 - num_count) % 3 != 0 and (input_num + 4 - num_count) % 5 != 0:
        print(input_num + 4 - num_count)


if __name__ == "__main__":
    main()
    