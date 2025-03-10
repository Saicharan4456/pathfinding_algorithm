import heapq

# Directional moves (8-connected: up, down, left, right, and the 4 diagonals)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1),  # 4 orthogonal directions
         (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 4 diagonal directions

# A* algorithm implementation
def a_star(grid, start, goal):
    # Helper function to calculate Manhattan distance (heuristic)
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority queue for open set (min-heap)
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))  # f, g, node

    # Dictionary for storing best g values (costs)
    g_costs = {start: 0}
    
    # Dictionary to store parent nodes for path reconstruction
    came_from = {}

    while open_set:
        # Get the current node with the lowest f value
        _, g, current = heapq.heappop(open_set)

        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path  # Return the reconstructed path

        # Explore neighbors
        for dx, dy in MOVES:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Check if neighbor is within grid bounds and not an obstacle
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g + 1  # Assume uniform cost (1 step to move)

                # If this is a better g value or the neighbor has not been visited
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    came_from[neighbor] = current
                    g_costs[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, tentative_g, neighbor))

    return None  # No path found

# Example usage
if __name__ == "__main__":
    # Define grid (0 is free, 1 is obstacle)
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)  # Start position (row, col)
    goal = (4, 4)   # Goal position (row, col)

    path = a_star(grid, start, goal)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
