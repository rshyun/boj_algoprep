import sys

def main():
    input = lambda: sys.stdin.readline().strip()

    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        importance_queue = list(map(int, input().split()))
        max_importance = max(importance_queue)
        
        queue_head_idx = 0
        print_cnt = 0
        
        while importance_queue[M] != -1:
            
            if importance_queue[queue_head_idx] == max_importance:
                importance_queue[queue_head_idx] = -1
                queue_head_idx = (queue_head_idx + 1) % N
                print_cnt += 1
                max_importance = max(importance_queue)
                
            elif importance_queue[queue_head_idx] == -1 or importance_queue[queue_head_idx] < max_importance:
                queue_head_idx = (queue_head_idx + 1) % N
                
        print(print_cnt)
        


if __name__ == "__main__":
    main()
    