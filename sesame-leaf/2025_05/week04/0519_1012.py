import sys

# data form : {(int, int): {"data":bool, "neighbor":[(int, int)]}}
def make_square_graph(input_coord:list[tuple[int, int]], width:int, height:int) -> dict[tuple[int, int], dict[str, any]]:
    graph = {(x, y):{"data":False, "neighbors":None} for x in range(width) for y in range(height)}
    
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
    
    for cabbage_coord in input_coord:
        graph[cabbage_coord]["data"] = True
            
    return graph

def BFS(graph:dict[tuple[int, int], dict[str, any]], start_vertex:tuple[int, int], visited_vertices:set[tuple[int, int]]) -> None:
    
    visited_vertices.add(start_vertex)
    
    vertex_queue = [start_vertex]
    for current_vertex in vertex_queue:
        for neighbor_vertex in graph[current_vertex]["neighbors"]:
            if (graph[neighbor_vertex]["data"] == True) and (neighbor_vertex not in visited_vertices):
                vertex_queue.append(neighbor_vertex)
                visited_vertices.add(neighbor_vertex)

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        
        cabbage_coords = []
        for _ in range(K):
            cabbage_coords.append(tuple(map(int, input().split())))
        graph = make_square_graph(cabbage_coords, M, N)
        
        worm_count = 0
        visited_vertices = set()
        for x in range(M):
            for y in range(N):
                if (graph[(x, y)]["data"] == True) and ((x, y) not in visited_vertices):
                    BFS(graph, (x, y), visited_vertices)
                    worm_count += 1
        print(worm_count)


if __name__ == "__main__":
    main()
    