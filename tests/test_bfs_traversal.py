import pytest
from src.bfs_traversal import breadth_first_search

def test_basic_bfs():
    """Test basic BFS traversal on a simple graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']

def test_single_node_graph():
    """Test BFS on a graph with only one node."""
    graph = {'X': []}
    result = breadth_first_search(graph, 'X')
    assert result == ['X']

def test_disconnected_graph():
    """Test BFS on a graph with disconnected nodes."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_invalid_start_node():
    """Test that a ValueError is raised when start node is not in graph."""
    graph = {'A': ['B'], 'B': ['A']}
    with pytest.raises(ValueError, match="Start node Z not found in graph"):
        breadth_first_search(graph, 'Z')

def test_invalid_graph_type():
    """Test that a TypeError is raised when graph is not a dictionary."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        breadth_first_search([], 'A')

def test_graph_with_multiple_paths():
    """Test BFS on a graph with multiple paths between nodes."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D']