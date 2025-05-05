import sys

if __name__ == "__main__":
    input = lambda: sys.stdin.readline().rstrip()
    
    N = int(input())
    target_series = [int(input()) for _ in range(N)]
    
    stack = [0]
    next_push = iter([i for i in range(1, N+1)])
    operation_order = []
    
    for x in target_series:
        
        while stack[-1] < x:
            stack.append(next(next_push))
            operation_order.append("+")
        
        if stack[-1] != x:
            print("NO")
            break
        else:
            stack.pop()
            operation_order.append("-")
        
    else:
        print("\n".join(operation_order))
        