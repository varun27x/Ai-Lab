from collections import defaultdict
def dfs(graph, start):
    visited = set([start])
    stack = [start]
    while stack:
        node = stack.pop()
        print(node)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

graph = defaultdict(list)
n = int(input("enter the number of edges: "))
for _ in range(n):-p
    u,v = map(int,input("enter the two nodes: ").split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("enter the starting node: "))

dfs(graph, start)

