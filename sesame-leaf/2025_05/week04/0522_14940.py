"""
    
    This problem is the same solution that is implemented in 0520_14940.py.
    But, this code is more efficient in terms of memory and time.
                    
    | code          | memory    | time      |
    | 0520_14940.py | 235724 KB | 2184 ms   |
    | 0522_14940.py | 39936  KB | 240  ms   |
    
    The reason why 0522_14940.py is faster is due to the implementation method of BFS() function and the representation method of node and edge.
    
    The BFS() function of 0520_14940.py performs a search for a general graph.
    However, the BFS() fuction of 0522_14940.py performs a search only for graphs in the form of a Cartesian coordinate system. 
    
"""

import sys
from collections import deque

def BFS(input_map:list[list[any]], start_node:tuple[int, int]) -> None:
    
    map_height = len(input_map)
    map_width = len(input_map[0])
    
    search_queue = deque([start_node])
    while search_queue:
        current_x, current_y = search_queue.popleft()
        current_distance = input_map[current_y][current_x]
                
        if current_x != 0:
            if input_map[current_y][current_x-1] == None:
                input_map[current_y][current_x-1] = current_distance + 1
                search_queue.append((current_x-1, current_y))
        if current_x != map_width-1:
            if input_map[current_y][current_x+1] == None:
                input_map[current_y][current_x+1] = current_distance + 1
                search_queue.append((current_x+1, current_y))
        if current_y != 0:
            if input_map[current_y-1][current_x] == None:
                input_map[current_y-1][current_x] = current_distance + 1
                search_queue.append((current_x, current_y-1))
        if current_y != map_height-1:
            if input_map[current_y+1][current_x] == None:
                input_map[current_y+1][current_x] = current_distance + 1
                search_queue.append((current_x, current_y+1))
    
    return None

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    # get data
    height, width = map(int, input().split())
    
    node_map = []
    start_node = None
    for y in range(height):
        node_map.append(input().split())
        
        for x in range(width):
            
            # insert None if node_map[y][x] is available land, and insert 0 if start land
            if node_map[y][x] == "1":
                node_map[y][x] = None
                
            elif node_map[y][x] == "2":
                node_map[y][x] = 0
                start_node = (x, y)
                
            elif node_map[y][x] == "0":
                node_map[y][x] = 0
                
    BFS(node_map, start_node)
    
    for row in node_map:
        
        # insert -1 if node_map[y][x] is None (can't visit)
        for x in range(width):
            if row[x] is None:
                row[x] = -1
        
        # print one row at node_map
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
    