import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Define possible operations
def S1(state):  return (4, state[1])  # Set X to 4
def S2(state):  return (state[0], 3)  # Set Y to 3
def Z1(state):  return (0, state[1])  # Set X to 0
def Z3(state):  return (state[0], 0)  # Set Y to 0
def T1(state):  # Transfer X to Y
    transfer = min(state[0], 3 - state[1])
    return (state[0] - transfer, state[1] + transfer)
def T2(state):  # Transfer Y to X
    transfer = min(state[1], 4 - state[0])
    return (state[0] + transfer, state[1] - transfer)

# Heuristic Function: Sum of Absolute Differences
def heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

# A* Search Algorithm
def astar(start, goal):
    open_list = []  # Priority queue (Min-Heap)
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start, None))  # (f(n), g(n), state, parent)
    parent_map = {start: None}
    g_values = {start: 0}
    explored_states = set()
    G = nx.DiGraph()

    while open_list:
        _, g, current, parent = heapq.heappop(open_list)  # Expand state with lowest f(n)

        if current in explored_states:
            continue
        explored_states.add(current)

        # Track the search tree
        if parent is not None:
            G.add_edge(parent, current)

        # Goal check
        if current == goal:
            solution_path = []
            while current is not None:
                solution_path.append(current)
                current = parent_map[current]
            solution_path.reverse()
            return G, solution_path, list(open_list)  # Return graph, solution path, and queue when goal found

        # Expand node and add neighbors
        for operation in [S1, S2, Z1, Z3, T1, T2]:
            new_state = operation(current)
            new_g = g + 1  # Assume uniform cost of 1 per move
            new_f = new_g + heuristic(new_state, goal)

            if new_state not in g_values or new_g < g_values[new_state]:
                heapq.heappush(open_list, (new_f, new_g, new_state, current))
                g_values[new_state] = new_g
                parent_map[new_state] = current

    return None, None, None  # No solution found

# Run A* Search
start_state = (4, 3)
goal_state = (2, 0)
G, solution_path, queue_when_found = astar(start_state, goal_state)

# Draw graph using networkx
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)  # Layout for better visualization

# Draw all nodes
nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", node_size=500)

# Highlight solution path
nx.draw_networkx_nodes(G, pos, nodelist=solution_path, node_color="green", node_size=700)

plt.savefig("a*.png")
plt.title("A* Search Tree for (2,0) from (4,3)")
plt.show()

# Output solution path and queue when solution is found

print("Solution Path:", solution_path)
print("Queue when solution was found:", queue_when_found)
