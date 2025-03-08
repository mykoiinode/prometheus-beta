import pytest
from src.shortest_path_maze import find_shortest_path

def test_basic_path():
    """Test a simple path with multiple routes"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4

def test_direct_path():
    """Test a direct path without obstacles"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4

def test_no_path_start_blocked():
    """Test when start is blocked"""
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_no_path_end_blocked():
    """Test when end is blocked"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(grid) == -1

def test_no_path_completely_blocked():
    """Test when there's no possible path"""
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_complex_path():
    """Test a more complex path with multiple obstacles"""
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert find_shortest_path(grid) == 6

def test_single_cell_grid():
    """Test a single cell grid"""
    grid = [[0]]
    assert find_shortest_path(grid) == 1

def test_empty_grid():
    """Test an empty grid"""
    grid = []
    assert find_shortest_path(grid) == -1

def test_invalid_grid():
    """Test a non-square grid"""
    with pytest.raises(ValueError):
        find_shortest_path([[0, 0], [0]])

def test_large_grid():
    """Test a larger grid with a path"""
    grid = [
        [0] * 10 for _ in range(10)
    ]
    grid[5][5] = 1  # add an obstacle
    assert find_shortest_path(grid) == 18  # expected path length