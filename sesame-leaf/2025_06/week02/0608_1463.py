def main():
    target_num = int(input())
    
    operation_num = [0] * (target_num+1)
    for current_num in range(2, target_num+1):
        
        min_cnt = operation_num[current_num - 1] + 1
        
        if current_num % 3 == 0:
            if operation_num[current_num // 3] + 1 < min_cnt:
                min_cnt = operation_num[current_num // 3] + 1
        
        if current_num % 2 == 0:
            if operation_num[current_num // 2] + 1 < min_cnt:
                min_cnt = operation_num[current_num // 2] + 1
        
        operation_num[current_num] = min_cnt
    
    print(operation_num[-1])
        
if __name__ == "__main__":
    main()
    