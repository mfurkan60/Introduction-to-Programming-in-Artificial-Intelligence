from collections import deque

def bfs(graph, start_node, goal_node):
    """
    Breadth-First Search algorithm implementation.

    Args:
        graph (dict): Adjacency list representation of the graph
                      (e.g., {'A': ['B', 'C'], 'B': ['D']})
        start_node: The starting node.
        goal_node: The target node to find.

    Returns:
        list: A list representing the path from start_node to goal_node,
              or None if no path exists.
    """
    if start_node == goal_node:
        return [start_node]

    # Queue stores tuples of (node, path_list_so_far)
    queue = deque([(start_node, [start_node])])
    visited = {start_node} # Set to keep track of visited nodes

    while queue:
        current_node, path = queue.popleft() # FIFO

        # Explore neighbors
        # Use graph.get(current_node, []) to handle nodes with no outgoing edges
        for neighbor in graph.get(current_node, []):
            if neighbor == goal_node:
                return path + [neighbor] # Path found

            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None # Path not found

# --- Example Usage ---
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    sample_graph = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']
    }

    start = 'G'
    goal = 'D'

    print(f"--- Breadth-First Search ---")
    print(f"Graph: {sample_graph}")
    print(f"Finding path from {start} to {goal}")

    path_result = bfs(sample_graph, start, goal)

    if path_result:
        print(f"Path found: {' -> '.join(path_result)}")
    else:
        print(f"No path found from {start} to {goal}.")

    print("-" * 20)

    start = 'A'
    goal = 'F'
    path_result = bfs(sample_graph, start, goal)
    if path_result:
        print(f"Finding path from {start} to {goal}")
        print(f"Path found: {' -> '.join(path_result)}")
    else:
        print(f"No path found from {start} to {goal}.")