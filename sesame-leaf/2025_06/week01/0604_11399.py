def main():
    _ = int(input())
    withdraw_time = enumerate(sorted([int(x) for x in input().split()], reverse=True))
    min_time = 0
    for i, time in withdraw_time:
        min_time += time * (i + 1)
        
    print(min_time)

if __name__ == "__main__":
    main()
    