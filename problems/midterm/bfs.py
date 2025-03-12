import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Define possible operations as functions
def S1(state):  # Set X to 4
    return (4, state[1])

def S2(state):  # Set Y to 3
    return (state[0], 3)

def Z1(state):  # Set X to 0
    return (0, state[1])

def Z3(state):  # Set Y to 0
    return (state[0], 0)

def T1(state):  # Transfer X to Y
    transfer = min(state[0], 3 - state[1])
    return (state[0] - transfer, state[1] + transfer)

def T2(state):  # Transfer Y to X
    transfer = min(state[1], 4 - state[0])
    return (state[0] + transfer, state[1] - transfer)

# Define BFS function to find solution
def bfs(start, goal):
    queue = deque([start])
    parent = {start: None}  # Track parent nodes
    expanded_states = []
    solution_path = []
    G = nx.DiGraph()  # Directed graph to store search tree

    while queue:
        current = queue.popleft()
        expanded_states.append(current)
        
        if current == goal:
            break

        # Apply all possible operations
        for operation in [S1, S2, Z1, Z3, T1, T2]:
            new_state = operation(current)
            if new_state not in parent:  # Avoid repeated states
                parent[new_state] = current
                queue.append(new_state)
                G.add_edge(current, new_state)  # Add edge to graph

    # Backtrack to find solution path
    state = goal
    while state is not None:
        solution_path.append(state)
        state = parent[state]
    solution_path.reverse()
    
    return G, expanded_states, solution_path

# Run BFS to find the solution
start_state = (0, 0)
goal_state = (2, 3)
G, expanded_states, solution_path = bfs(start_state, goal_state)

# Draw graph using networkx
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)  # Layout for better visualization

# Draw all nodes
nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", node_size=500)

# Highlight expanded states
nx.draw_networkx_nodes(G, pos, nodelist=expanded_states, node_color="blue", node_size=700)

# Highlight solution path
nx.draw_networkx_nodes(G, pos, nodelist=solution_path, node_color="green", node_size=700)

plt.savefig("bfs.png")  # Saves the figure as an image
plt.title("State-Space Search Tree (BFS) for (2,3)")
plt.show()

# Output expanded states count
print("Minimum states expanded:", len(expanded_states))
print("Maximum states expanded:", len(G.nodes))
