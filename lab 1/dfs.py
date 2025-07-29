def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

def graph(n):
    graph = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        graph[key] = value
    return graph

n = int(input('enter the number of nodes: '))

dfs(graph(n), 'A')

