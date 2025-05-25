import sys

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    population = int(input())
    # list[input order, tuple[weight, height], None(space for size grade)]
    # sort by (weight, height) reversed
    datas = sorted([[idx, tuple(map(int, input().split())), 0] for idx in range(population)], key=lambda x: x[1], reverse=True)
    
    for current_idx in range(len(datas)):
        for compare_idx in range(current_idx):
            
            if datas[compare_idx][1][0] == datas[current_idx][1][0]:
                break
            
            if (datas[compare_idx][1][0] > datas[current_idx][1][0]) and (datas[compare_idx][1][1] > datas[current_idx][1][1]):
                datas[current_idx][2] += 1
    
    # sort by the order of input
    datas.sort(key=lambda x: x[0])
    for x in datas:
        print(x[2]+1, end=" ")

if __name__ == "__main__":
    main()
    