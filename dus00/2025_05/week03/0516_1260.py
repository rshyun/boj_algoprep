from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

def dfs(v):
    visited1[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if graph[v][i] == 1 and not visited1[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = 1
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in range(1, n + 1):
            if graph[cur][i] == 1 and not visited2[i]:
                queue.append(i)
                visited2[i] = 1

if __name__ == "__main__":
    dfs(v)
    print()
    bfs(v)