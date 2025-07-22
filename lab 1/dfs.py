def dfs(node, graph, visited, component):
    component.append(node)
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child, graph, visited, component)

if __name__ == "__main__":

    n = int(input("Enter number of nodes: "))
    graph = {}

    for i in range(n):
        edges = input(f"Enter adjacent nodes for node {i} (space-separated): ")
        graph[i] = list(map(int, edges.strip().split()))

    visited = {node: False for node in graph}
    components = []

    for node in graph:
        if not visited[node]:
            component = []
            dfs(node, graph, visited, component)
            components.append(component)

    for i, comp in enumerate(components):
        print(f"Component {i+1} : {comp}")

# 4
# 0
# 1 3
# 1 2
# 3
