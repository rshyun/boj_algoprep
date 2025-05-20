def main():
    way_count = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for current_num in range(1, 12):
        for atomic_num in [1, 2, 3]:
            if current_num - atomic_num >= 0:
                way_count[current_num] += way_count[current_num - atomic_num]

    for _ in range(int(input())):
        print(way_count[int(input())])
        

if __name__ == "__main__":
    main()
    