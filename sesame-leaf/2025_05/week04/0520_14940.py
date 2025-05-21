import sys

# data form : dict[vertex(any):dict["neighbor":list[any]]]
def make_graph(input_vertices:list[tuple[any, any]]) -> dict[any, dict[str, any]]:
    graph = dict()
    
    for start_vertex, end_vertex in input_vertices:
        if start_vertex not in graph:
            graph[start_vertex] = {"neighbors":[end_vertex]}
        else:
            graph[start_vertex]["neighbors"].append(end_vertex)
    
    return graph

def make_square_graph(width:int, height:int) -> dict[tuple[int, int], dict[str, list[tuple[int, int]]]]:
    graph = {(x, y):{"neighbors":None} for x in range(width) for y in range(height)}
    
    for x in range(width):
        for y in range(height):
            neighbor_list = []
            if x != 0:
                neighbor_list.append((x-1, y))
            if x != width-1:
                neighbor_list.append((x+1, y))
            if y != 0:
                neighbor_list.append((x, y-1))
            if y != height-1:
                neighbor_list.append((x, y+1))
            graph[(x, y)]["neighbors"] = neighbor_list
            
    return graph

def BFS(graph:dict[any, dict[str, any]], start_vertex:any) -> list[any]:
    
    visited_vertices = set([start_vertex])
    
    vertex_queue = [start_vertex]
    search_order = []
    for current_vertex in vertex_queue:
        search_order.append(current_vertex)
        for neighbor_vertex in graph[current_vertex]["neighbors"]:
            if neighbor_vertex not in visited_vertices:
                vertex_queue.append(neighbor_vertex)
                visited_vertices.add(neighbor_vertex)
    
    return search_order

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    height, width = map(int, input().split())
    
    data = []
    for _ in range(height):
        data.append(list(map(int, input().split())))
    
    map_graph = make_square_graph(width, height)
    start_vertex = None
    for y in range(height):
        for x in range(width):
            if data[y][x] == 0:
                # delete the vertex (x, y)
                for neighbor_vertex in map_graph[(x, y)]["neighbors"]:
                    map_graph[neighbor_vertex]["neighbors"].pop(map_graph[neighbor_vertex]["neighbors"].index((x, y)))
                    
                del map_graph[(x, y)]
                
            elif data[y][x] == 1:
                # add "distance" key
                map_graph[(x, y)]["distance"] = None
                
            elif data[y][x] == 2:
                # add "distance" key and initialize to 0
                start_vertex = (x, y)
                map_graph[start_vertex]["distance"] = 0
    
    map_search_order = BFS(map_graph, start_vertex)
    
    for current_vertex in map_search_order:
        
        for neighbor_vertex in map_graph[current_vertex]["neighbors"]:
            
            if map_graph[neighbor_vertex]["distance"] is None:
                map_graph[neighbor_vertex]["distance"] = map_graph[current_vertex]["distance"] + 1
                
    
    for y in range(height):
        for x in range(width):
            if (x, y) not in map_graph:
                print(0, end=" ")
            elif map_graph[(x, y)]["distance"] is None:
                print(-1, end=" ")
            else:
                print(map_graph[(x, y)]["distance"], end=" ")
        print()

if __name__ == "__main__":
    main()
    