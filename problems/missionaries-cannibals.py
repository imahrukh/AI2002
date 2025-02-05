import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Define the problem constraints
START_STATE = (3, 3, 1, 0, 0, 0)  # (M_left, C_left, B_left, M_right, C_right, B_right)
GOAL_STATE = (0, 0, 0, 3, 3, 1)

# Possible boat moves
MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # (Missionaries, Cannibals)

def is_valid_state(state):
    """Check if the state is valid and safe."""
    m_left, c_left, _, m_right, c_right, _ = state
    # Missionaries should not be outnumbered where they exist
    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return False
    return True

def get_successors(state):
    """Generate valid successor states from the current state."""
    successors = []
    m_left, c_left, b_left, m_right, c_right, b_right = state

    if b_left == 1:  # Boat is on the left side
        for m, c in MOVES:
            new_state = (m_left - m, c_left - c, 0, m_right + m, c_right + c, 1)
            if min(new_state) >= 0 and is_valid_state(new_state):
                successors.append(new_state)
    else:  # Boat is on the right side
        for m, c in MOVES:
            new_state = (m_left + m, c_left + c, 1, m_right - m, c_right - c, 0)
            if min(new_state) >= 0 and is_valid_state(new_state):
                successors.append(new_state)

    return successors

def bfs():
    """Breadth-First Search implementation."""
    queue = deque([(START_STATE, [])])
    visited = set()
    graph = nx.DiGraph()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state == GOAL_STATE:
            return path + [state], graph

        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path + [state]))
                graph.add_edge(state, successor)

    return None, graph

def dfs():
    """Depth-First Search implementation."""
    stack = [(START_STATE, [])]
    visited = set()
    graph = nx.DiGraph()

    while stack:
        state, path = stack.pop()
        if state in visited:
            continue
        visited.add(state)

        if state == GOAL_STATE:
            return path + [state], graph

        for successor in get_successors(state):
            if successor not in visited:
                stack.append((successor, path + [state]))
                graph.add_edge(state, successor)

    return None, graph

def depth_limited_dfs(state, path, depth, visited, graph):
    """Helper function for iterative deepening search."""
    if depth == 0:
        return None
    if state == GOAL_STATE:
        return path + [state]
    visited.add(state)

    for successor in get_successors(state):
        if successor not in visited:
            graph.add_edge(state, successor)
            result = depth_limited_dfs(successor, path + [state], depth - 1, visited, graph)
            if result:
                return result

    visited.remove(state)
    return None

def iterative_deepening_search():
    """Iterative Deepening Search (IDS) implementation."""
    depth = 0
    graph = nx.DiGraph()

    while True:
        visited = set()
        result = depth_limited_dfs(START_STATE, [], depth, visited, graph)
        if result:
            return result, graph
        depth += 1

def draw_graph(graph, title):
    """Draws the state space graph."""
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=8, edge_color="gray")
    plt.title(title)
    plt.show()

# Run BFS, DFS, and IDS
bfs_path, bfs_graph = bfs()
dfs_path, dfs_graph = dfs()
ids_path, ids_graph = iterative_deepening_search()

# Draw the graphs
draw_graph(bfs_graph, "Breadth-First Search (BFS) State Space")
draw_graph(dfs_graph, "Depth-First Search (DFS) State Space")
draw_graph(ids_graph, "Iterative Deepening Search (IDS) State Space")

# Print the solution paths
print("\nBFS Solution Path:", bfs_path)
print("DFS Solution Path:", dfs_path)
print("IDS Solution Path:", ids_path)
