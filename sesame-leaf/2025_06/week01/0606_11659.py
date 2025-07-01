import sys

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    num_num, result_num = map(int, input().split())
    nums = [0] + list(map(int, input().split()))
    
    sums = [0] * (num_num + 1)
    for i in range(1, num_num+1):
        sums[i] = sums[i-1] + nums[i]
        
    for _ in range(result_num):
        start, end = map(int, input().split())
        print(sums[end] - sums[start-1])
        
if __name__ == "__main__":
    main()
    