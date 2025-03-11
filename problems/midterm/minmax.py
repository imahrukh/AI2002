import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Minimax values for backpropagation
minimax_values = {}

# Function to create the game tree
def build_game_tree(N, player, parent=None):
    """
    Builds the game tree for the minimax decision.
    N: Current game state (remaining value)
    player: 'Program' or 'Opponent'
    parent: Parent node in the tree
    """
    node_name = f"{player} (N={N})"
    
    # If N is 0, this is a leaf node, determine winner
    if N == 0:
        value = -1 if player == "Program" else +1  # Program loses if it moves to N=0
        minimax_values[node_name] = value
        return
    
    # Add the node to the graph
    if parent:
        G.add_edge(parent, node_name)
    
    # Generate children nodes for possible moves (1, 2, 3)
    possible_moves = [i for i in [1, 2, 3] if i <= N]
    
    for move in possible_moves:
        next_player = "Opponent" if player == "Program" else "Program"
        build_game_tree(N - move, next_player, node_name)

# Build the tree from N=5 (Program's Turn)
build_game_tree(5, "Program")

# Minimax Value Propagation
def minimax(node):
    """ Recursively assigns minimax values to each node """
    if node in minimax_values:  # Leaf node
        return minimax_values[node]
    
    children = list(G.successors(node))
    
    if not children:
        return 0  # Draw (shouldn't happen in this game)
    
    values = [minimax(child) for child in children]
    
    if "Program" in node:  # Maximizing for Program
        minimax_values[node] = max(values)
    else:  # Minimizing for Opponent
        minimax_values[node] = min(values)
    
    return minimax_values[node]

# Compute minimax values
minimax("Program (N=5)")

# Draw the tree
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)  # Layout for graph positioning
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=8, font_weight="bold", edge_color="gray")

# Add minimax values as labels
labels = {node: f"{node}\n({minimax_values.get(node, '')})" for node in G.nodes}
nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight="bold")

plt.title("Minimax Game Tree (N=5)")
plt.show()
