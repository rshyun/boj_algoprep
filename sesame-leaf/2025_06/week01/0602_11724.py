import sys

# convert [(start_node, end_node)] form to {start_node : [neighbors]}
def make_bi_graph(edge_info:list[tuple[int, int]]) -> dict[int, list[int]]:
    result_graph = dict()
    
    for current_edge in edge_info:
        start_node, end_node = current_edge
        
        if start_node not in result_graph:
            result_graph[start_node] = [end_node]
        else:
            result_graph[start_node].append(end_node)
        
        if end_node not in result_graph:
            result_graph[end_node] = [start_node]
        else:
            result_graph[end_node].append(start_node)
        
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
    
    node_num, edge_num = map(int, input().split())
    
    edges = [tuple(map(int, input().split())) for _ in range(edge_num)]
    graph = make_bi_graph(edges)
    
    connected_component_count = 0
    visited_nodes = set()
    for node in graph:
        if node not in visited_nodes:
            connected_component_count += 1
            DFS(graph, node, visited_nodes)
            
    print(connected_component_count + (node_num - len(graph)))

if __name__ == "__main__":
    main()
    