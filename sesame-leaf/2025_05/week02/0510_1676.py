def main():
    
    N = int(input())
    
    cnt_of_2 = 0
    cnt_of_5 = 0
    for x in range(1, N+1):
        
        while x % 2 == 0:
            x //= 2
            cnt_of_2 += 1
            
        while x % 5 == 0:
            x //= 5
            cnt_of_5 += 1
            
    print(min(cnt_of_2, cnt_of_5))
        

if __name__ == "__main__":
    main()
