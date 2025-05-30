import sys

def Heap_add(heap_list:list[int], add_num:int) -> None:
    
    heap_list.append(add_num)
    
    child_idx = len(heap_list) - 1
    parent_idx = child_idx // 2
    while parent_idx != 0:
        if heap_list[child_idx] < heap_list[parent_idx]:
            heap_list[child_idx], heap_list[parent_idx] = heap_list[parent_idx], heap_list[child_idx]
            
            child_idx = parent_idx
            parent_idx //= 2
        else:
            break
            
    return None

def Heap_pop(heap_list:list[int]) -> int:
    
    if len(heap_list) == 1:
        return 0
    
    return_num = heap_list[1]
    heap_list[1] = heap_list[-1]
    heap_list.pop()
    
    parent_idx = 1
    # 0 is not real child index. It's just for declareation of child_idx
    child_idx = 0
    
    # parent node의 왼쪽 node가 존재하면 실행함.
    # execute only when left node of parent node exist.
    while ((parent_idx*2) <= (len(heap_list)-1)):
        
        # parent node의 오른쪽 node가 존재할 때
        # when right node of parent node exist
        if ((parent_idx*2)+1) <= (len(heap_list)-1):
            child_idx = (parent_idx*2) if heap_list[(parent_idx*2)] < heap_list[(parent_idx*2)+1] else ((parent_idx*2)+1)
            
        # parent node의 오른쪽 node가 존재하지 않을 때
        # when right node of parent node doesn't exist
        else:
            child_idx = parent_idx * 2
            
        if heap_list[parent_idx] > heap_list[child_idx]:
            heap_list[child_idx], heap_list[parent_idx] = heap_list[parent_idx], heap_list[child_idx]
            
            parent_idx = child_idx
        else:
            break
    
    return return_num

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    operation_num = int(input())
    
    heap_list = [0]
    result = []
    for _ in range(operation_num):
        input_num = int(input())
        
        if input_num == 0:
            result.append(Heap_pop(heap_list))
        else:
            Heap_add(heap_list, input_num)
    
    print("\n".join(map(str, result)))
            
if __name__ == "__main__":
    main()
    