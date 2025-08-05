import heapq

def uniform_cost_search(graph, start, goal):

    frontier = [(0, start, [])]
    explored = set()

    while frontier:
        cost, current_node, path = heapq.heappop(frontier)

        if current_node in explored:
            continue

        path = path + [current_node]
        explored.add(current_node)

        if current_node == goal:
            return path, cost

        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + edge_cost, neighbor, path))

    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

path, cost = uniform_cost_search(graph, 'A', 'G')
print("Optimal path:", path)
print("Total cost:", cost)