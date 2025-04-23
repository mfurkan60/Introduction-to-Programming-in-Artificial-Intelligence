import heapq # For the priority queue

def heuristic(a, b):
    """
    Calculate the Manhattan distance heuristic between two points (tuples).
    Args:
        a (tuple): (row, col) of the first point.
        b (tuple): (row, col) of the second point.
    Returns:
        int: The Manhattan distance.
    """
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current):
    """Reconstructs the path from start to goal."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1] # Return reversed path

def get_neighbors(grid, node):
    """Gets valid neighbors (up, down, left, right) for a node in the grid."""
    rows, cols = len(grid), len(grid[0])
    r, c = node
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Right, Left, Down, Up
        nr, nc = r + dr, c + dc
        # Check bounds and if it's not an obstacle (assuming 1 is obstacle)
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
            neighbors.append((nr, nc))
    return neighbors

def a_star_search(grid, start, goal):
    """
    A* Search algorithm implementation for a grid.

    Args:
        grid (list[list[int]]): 2D list representing the grid.
                                0 represents walkable path, 1 represents obstacle.
        start (tuple): (row, col) of the starting position.
        goal (tuple): (row, col) of the goal position.

    Returns:
        list: A list of tuples representing the path from start to goal,
              or None if no path exists.
    """
    rows = len(grid)
    cols = len(grid[0])

    # Check if start or goal are obstacles
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None

    # Priority queue stores tuples: (f_score, node)
    open_set = [(heuristic(start, goal), start)] # Start with f_score = h(start) since g(start)=0
    heapq.heapify(open_set)

    # Dictionary to reconstruct the path: came_from[node] = previous_node
    came_from = {}

    # g_score[node] = cost from start to node
    g_score = { (r, c): float('inf') for r in range(rows) for c in range(cols) }
    g_score[start] = 0

    # f_score[node] = g_score[node] + h(node)
    # We can derive f_score when needed or store it. Storing g_score is sufficient.
    # The priority queue effectively stores f_score.

    open_set_hash = {start} # Keep track of items in the priority queue for quick lookups

    while open_set:
        # Get node with the lowest f_score from priority queue
        current_f, current_node = heapq.heappop(open_set)
        open_set_hash.remove(current_node)

        if current_node == goal:
            return reconstruct_path(came_from, current_node) # Path found!

        # Explore neighbors
        for neighbor in get_neighbors(grid, current_node):
            # Assume cost between adjacent cells is 1
            tentative_g_score = g_score[current_node] + 1

            if tentative_g_score < g_score[neighbor]:
                # This path to neighbor is better than any previous one. Record it.
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)

                # If neighbor not in open_set add it. heapq handles priority.
                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f_score, neighbor))
                    open_set_hash.add(neighbor)
                # Note: If neighbor is already in open_set with higher f_score,
                # heapq doesn't update priorities directly. Pushing the new lower
                # f_score tuple works because it will be popped earlier.
                # The higher f_score version will eventually be popped and ignored
                # because its g_score will be higher than the updated one.

    return None # Path not found

# --- Example Usage ---
if __name__ == "__main__":
    # Example grid (0: walkable, 1: obstacle)
    grid_map = [
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
    ]

    start_pos = (0, 0)
    goal_pos = (4, 5)

    print(f"--- A* Search ---")
    print("Grid Map (0=walkable, 1=obstacle):")
    for row in grid_map:
        print(row)
    print(f"Finding path from {start_pos} to {goal_pos}")

    path_result = a_star_search(grid_map, start_pos, goal_pos)

    if path_result:
        print(f"Path found: {path_result}")
        # Optional: Visualize path on the grid
        print("\nPath Visualization (*=path, S=start, G=goal):")
        vis_grid = [list(row) for row in grid_map] # Create a mutable copy
        for r, c in path_result:
            if (r, c) != start_pos and (r, c) != goal_pos:
                vis_grid[r][c] = '*'
        vis_grid[start_pos[0]][start_pos[1]] = 'S'
        vis_grid[goal_pos[0]][goal_pos[1]] = 'G'
        for row in vis_grid:
            print(" ".join(map(str, row)))

    else:
        print(f"No path found from {start_pos} to {goal_pos}.")

    print("-" * 20)

    # Example with no path
    goal_pos_no_path = (1, 2) # Inside an obstacle area
    print(f"Finding path from {start_pos} to {goal_pos_no_path}")
    path_result_no = a_star_search(grid_map, start_pos, goal_pos_no_path)
    if path_result_no:
         print(f"Path found: {path_result_no}")
    else:
        print(f"No path found from {start_pos} to {goal_pos_no_path}.")