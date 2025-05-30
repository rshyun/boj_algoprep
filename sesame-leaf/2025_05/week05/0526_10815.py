import sys
    
def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    _ = input()
    data_set = set(input().split())
    _ = input()
    search_list = input().split()
    
    print(" ".join(["1" if target in data_set else "0" for target in search_list]))

if __name__ == "__main__":
    main()
    