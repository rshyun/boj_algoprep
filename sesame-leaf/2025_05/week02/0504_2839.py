import sys

if __name__ == "__main__":
    
    input = lambda: sys.stdin.readline().rstrip()
    
    N = int(input())
    
    for a in range(N//5, -1, -1):
        
        if (N-5*a) % 3 == 0:
            print(a+((N-5*a) // 3))
            break
        
        if a == 0:
            print(-1)
            