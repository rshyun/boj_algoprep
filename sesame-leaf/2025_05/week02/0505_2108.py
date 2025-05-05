import sys

if __name__ == "__main__":
    
    input = lambda: sys.stdin.readline().rstrip()
    
    N = int(input())
    
    # num_dict의 구조는 {xi:fi}의 구조를 가지고 있다.
    num_dict = {}
    num_list = []
    data_sum = 0
    for _ in range(N):
        
        input_num = int(input())
        
        if input_num in num_dict:
            num_dict[input_num] += 1
        else:
            num_dict[input_num] = 1
        
        num_list.append(input_num)
        
        data_sum += input_num
    
    num_list.sort()
    
    data_mean = round(data_sum / N)
    data_median = num_list[N//2]
    temp = sorted(num_dict.items(), key=lambda x: (x[1], -1*x[0])) if N != 1 else list(num_dict.items())
    data_mode = (temp[-1][0] if temp[-1][1] != temp[-2][1] else temp[-2][0]) if N != 1 else temp[0][0]
    data_range = num_list[-1] - num_list[0]
    
    print(f"{data_mean}\n{data_median}\n{data_mode}\n{data_range}")
