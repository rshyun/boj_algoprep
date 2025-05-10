import sys

def is_prime(input_int=int):
    
    if input_int == 1:
        return False
    
    for i in range(2, int(input_int**0.5)+1):
        if input_int % i == 0:
            return False
    return True


def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    M, N = map(int, input().split())

    for i in range(M, N+1):
        if is_prime(i):
            print(i)
            

if __name__ == "__main__":
    main()
            