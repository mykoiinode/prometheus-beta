from typing import List
from collections import deque

def find_shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path from top-left to bottom-right in a 2D grid maze.
    
    Args:
        grid (List[List[int]]): A 2D grid where 0 represents open paths and 1 represents walls.
                                Grid is NxN square.
    
    Returns:
        int: Length of the shortest path from top-left to bottom-right, 
             or -1 if no path exists.
    
    Raises:
        ValueError: If the grid is empty or not a square matrix.
    """
    # Validate input
    if not grid or not grid[0]:
        return -1
    
    # Check if grid is square
    n = len(grid)
    if any(len(row) != n for row in grid):
        raise ValueError("Grid must be a square matrix")
    
    # If start or end is blocked, no path exists
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Possible moves: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # BFS to find shortest path
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    visited = set([(0, 0)])
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right
        if row == n-1 and col == n-1:
            return path_length
        
        # Try all 4 directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                queue.append((new_row, new_col, path_length + 1))
                visited.add((new_row, new_col))
    
    # No path found
    return -1