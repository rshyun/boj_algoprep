import sys

def cut_wire_count(standard_len:int, len_of_wires:list[int]) -> int:
    return sum([wire_len // standard_len for wire_len in len_of_wires])

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    K, N = map(int, input().split())
    
    len_of_wires = []
    for _ in range(K):
        len_of_wires.append(int(input()))
        
    left_point = 1
    right_point = max(len_of_wires)
    result = -1
    while left_point <= right_point:
        
        middle_point = (left_point + right_point) // 2
        wire_count = cut_wire_count(middle_point, len_of_wires)
        
        if wire_count >= N:
            result = middle_point
            left_point = middle_point + 1
        elif wire_count < N:
            right_point = middle_point - 1
    
    print(result)
        
    
if __name__ == "__main__":
    main()
    