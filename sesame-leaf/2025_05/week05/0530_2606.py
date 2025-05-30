import sys

# convert [(start_node, end_node)] form to {start_node : [neighbors]}
def make_bi_graph(nodes:list[int], edge_info:list[tuple[int, int]]) -> dict[int, list[int]]:
    result_graph = dict({node:[] for node in nodes})
    
    for current_edge in edge_info:
        result_graph[current_edge[0]].append(current_edge[1])
        result_graph[current_edge[1]].append(current_edge[0])
        
    return result_graph

def DFS(graph:dict[int, list[int]], start_node:int, visited:set[int]) -> None:
    
    stack = list([start_node])
    
    while stack:
        current_node = stack.pop()
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                stack.append(neighbor)
                
    return None

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    node_num = int(input())
    edge_num = int(input())
    
    edges = [tuple(map(int, input().split())) for _ in range(edge_num)]
    graph = make_bi_graph([x for x in range(1, node_num+1)], edges)
    
    visited_nodes = set()
    DFS(graph, 1, visited_nodes)
    
    print(len(visited_nodes)-1)

if __name__ == "__main__":
    main()
    