import sys

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    T = int(input())
    input_nums = [int(input()) for _ in range(T)]
    max_num = max(input_nums)
    
    z_o_nums = [(1, 0), (0, 1)] + [None] * (max_num-1)
    
    for current_num in range(2, max_num+1):
        z_o_nums[current_num] = (z_o_nums[current_num-1][0]+z_o_nums[current_num-2][0], z_o_nums[current_num-1][1]+z_o_nums[current_num-2][1])
    
    for input_num in input_nums:
        print(*z_o_nums[input_num])

if __name__ == "__main__":
    main()
    