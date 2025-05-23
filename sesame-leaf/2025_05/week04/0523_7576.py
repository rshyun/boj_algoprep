import sys
from collections import deque

def BFS_one_cycle(input_map:list[list[any]], queue:deque[tuple[int, int]]) -> None:
    
    for _ in range(len(queue)):
        current_x, current_y = queue.popleft()
                
        if (current_x != 0) and (input_map[current_y][current_x-1] == False):
                input_map[current_y][current_x-1] = True
                queue.append((current_x-1, current_y))
                
        if (current_x != len(input_map[0])-1) and (input_map[current_y][current_x+1] == False):
                input_map[current_y][current_x+1] = True
                queue.append((current_x+1, current_y))
                
        if (current_y != 0) and (input_map[current_y-1][current_x] == False):
                input_map[current_y-1][current_x] = True
                queue.append((current_x, current_y-1))
                
        if current_y != len(input_map)-1 and (input_map[current_y+1][current_x] == False):
                input_map[current_y+1][current_x] = True
                queue.append((current_x, current_y+1))
    
    return None

def BFS_cycle_count(input_map:list[list[any]], start_nodes:list[(int, int)]) -> int:
    
    search_queue = deque(start_nodes)
    cycle_count = 0
    while search_queue:
        BFS_one_cycle(input_map, search_queue)
        cycle_count += 1
    
    return cycle_count


def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    box_width, box_height = map(int, input().split())
    
    box = list()
    riped_tomatoes = list()
    for y in range(box_height):
        row = input().split()
        
        for x in range(box_width):  
            # there is no tomato        : None
            # there is riped tomato     : True
            # there is unriped tomato   : False
            if row[x] == "-1":
                row[x] = None
            elif row[x] == "0":
                row[x] = False
            elif row[x] == "1":
                row[x] = True
                riped_tomatoes.append((x, y))
                
        box.append(row)
    
    
    day_count = BFS_cycle_count(box, riped_tomatoes) - 1
    
    
    there_is_unriped_tomato = False
    for row in box:
        for this_tomato_riped in row:
            if (this_tomato_riped is not None) and (not this_tomato_riped):
                there_is_unriped_tomato = True
                break
        
        if there_is_unriped_tomato:
            break
    
    
    if there_is_unriped_tomato:
        print(-1)
    else:
        print(day_count)

if __name__ == "__main__":
    main()
    