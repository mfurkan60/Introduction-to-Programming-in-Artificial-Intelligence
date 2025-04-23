 
def dfs_iterative(graph, start_node, goal_node):
    """
    Iterative Depth-First Search algorithm implementation using a stack.

    Args:
        graph (dict): Adjacency list representation of the graph.
        start_node: The starting node.
        goal_node: The target node to find.

    Returns:
        list: A list representing the path from start_node to goal_node,
              or None if no path exists.
    """
    if start_node == goal_node:
        return [start_node]

    # Stack stores tuples of (node, path_list_so_far)
    stack = [(start_node, [start_node])]
    visited = set() # Keep track of visited nodes to prevent cycles in this path search

    while stack:
        (current_node, path) = stack.pop() # LIFO

        # If we've already visited this node via potentially another path,
        # skip it to avoid cycles and redundant work in *this specific search*.
        # Note: In pure graph traversal DFS you might only add to visited here.
        # For path finding, adding earlier prevents cycles in the path.
        if current_node in visited:
             continue
        visited.add(current_node)


        if current_node == goal_node:
            return path # Path found

        # Explore neighbors - push them onto the stack in reverse order
        # so they are popped in the original order (optional, affects path found)
        # Use graph.get(current_node, []) to handle nodes with no outgoing edges
        for neighbor in reversed(graph.get(current_node, [])):
             if neighbor not in visited: # Only add unvisited neighbors to the stack for path finding
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))


    return None # Path not found

# --- Example Usage ---
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    sample_graph = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'], # Added E neighbor for D
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']
    }

    start = 'G'
    goal = 'D'

    print(f"--- Depth-First Search (Iterative) ---")
    print(f"Graph: {sample_graph}")
    print(f"Finding path from {start} to {goal}")

    path_result = dfs_iterative(sample_graph, start, goal)

    if path_result:
        print(f"Path found: {' -> '.join(path_result)}")
    else:
        print(f"No path found from {start} to {goal}.")

    print("-" * 20)

    start = 'A'
    goal = 'F'
    path_result = dfs_iterative(sample_graph, start, goal)
    if path_result:
        print(f"Finding path from {start} to {goal}")
        print(f"Path found: {' -> '.join(path_result)}")
    else:
        print(f"No path found from {start} to {goal}.")