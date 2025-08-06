from collections import deque

def bfs(graph,start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = defaultdict(list)
n = input("enter the number of edges"))
for _ in range(n):
    u,v = map(int,input("enter the two nodes: ").split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("enter the first node: "))
    
bfs(graph, start)
