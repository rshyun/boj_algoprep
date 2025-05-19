# 알게된 점: 처음에는 입력받은 graph를 직접 수정해가면서 DFS, BFS의 순서를 구했는데(백준 제출번호: 94430907 에서 확인 가능), 그렇게 하면 오류의 가능성이 높아짐. 따라서 입력받은 값은 변경하지 않고 답을 return 해야함.
# 도움: chatGPT
import sys

def make_graph(input:list[tuple[int, int]], vertex_num:int) -> dict[int, list[int]]:
    graph = {i:[] for i in range(1, vertex_num+1)}
    for start, end in list(set(input)):
        graph[start].append(end)
    
    return graph

def make_bi_graph(input:list[tuple[int, int]], vertex_num:int) -> dict[int, list[int]]:
    graph = {i:[] for i in range(1, vertex_num+1)}
    for start, end in input:
        graph[start].append(end)
        graph[end].append(start)
            
    return graph

def sort_graph(input:dict[int, list[int]]) -> None:
    for lists in input.values():
        lists.sort()


def DFS(graph:dict[int, list[int]], start_vertex:int, visited_vertices:set=None) -> list[int]:
    
    if visited_vertices is None:
        visited_vertices = set([start_vertex])
    
    search_order = [start_vertex]
    for child_vertex in graph[start_vertex]:
        if child_vertex not in visited_vertices:
            visited_vertices.add(child_vertex)
            search_order.extend(DFS(graph, child_vertex, visited_vertices))
    
    return search_order

def BFS(graph:dict[int, list[int]], start_vertex:int) -> list[int]:
    
    visited_vertices = set([start_vertex])
    
    vertex_queue = [start_vertex]
    search_order = []
    for current_vertex in vertex_queue:
        search_order.append(current_vertex)
        for neighbor_vertex in graph[current_vertex]:
            if neighbor_vertex not in visited_vertices:
                vertex_queue.append(neighbor_vertex)
                visited_vertices.add(neighbor_vertex)
    
    return search_order


def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    N, M, V = map(int, input().split())
    graph = make_bi_graph([tuple(map(int, input().split())) for _ in range(M)], N)
    sort_graph(graph)
    
    print(f"{" ".join(map(str, DFS(graph, V)))}\n{" ".join(map(str, BFS(graph, V)))}")


if __name__ == "__main__":
    main()
    