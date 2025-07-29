from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            queue.extend(graph[node])

def graph(n):
    graph = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        graph[key] = value
    return graph

n = int(input('enter the number of nodes: '))

bfs(graph, 'A')
