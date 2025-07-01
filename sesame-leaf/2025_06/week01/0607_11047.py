import sys

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    coin_num, goal_value = map(int, input().split())
    coin_values = reversed(list([int(input()) for _ in range(coin_num)]))
    
    used_coin_num = 0
    for coin_value in coin_values:
        
        if goal_value < coin_value:
            continue
        
        used_coin_num += goal_value // coin_value
        goal_value = goal_value % coin_value
    
    print(used_coin_num)
        
if __name__ == "__main__":
    main()
    