import heapq

# Knight's possible move directions
moves = [
    (2, 1), (2, -1),
    (-2, 1), (-2, -1),
    (1, 2), (1, -2),
    (-1, 2), (-1, -2)
]

def print_current_state(level, x, y, visited):
    """Print current node state in a simple format"""
    print(f"Level {level}: Position ({x},{y}), Visited {sum(visited)} squares")
    print("Board State:")
    for i in range(8):
        row = ['#' if visited[i*8 + j] else '.' for j in range(8)]
        row[y] = 'K' if i == x else row[y]
        row = ' '.join(row)
        print(row)
    print("\n")

def calculate_moves(x, y, visited):
    """Calculate number of possible moves using Warnsdorf's rule"""
    count = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx*8 + ny]:
            count += 1
    return count

def get_successors(x, y, visited):
    """Generate valid successor moves"""
    successors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx*8 + ny]:
            new_visited = visited.copy()
            new_visited[nx*8 + ny] = True
            successors.append((nx, ny, new_visited))
    return successors

# Iterative Deepening Search
def iterative_deepening(start_x, start_y):
    initial_visited = [False]*64
    initial_visited[start_x*8 + start_y] = True
    
    for depth in range(1, 65):
        result = depth_limited_search(start_x, start_y, initial_visited, [(start_x, start_y)], depth)
        if result:
            return result
    return None

def depth_limited_search(x, y, visited, path, limit):
    current_level = len(path)
    print(f"IDS: Trying depth {current_level}")
    print_current_state(current_level, x, y, visited)
    
    if current_level == 64:
        return path
    
    if current_level >= limit:
        return None
    
    for nx, ny, new_vis in get_successors(x, y, visited):
        result = depth_limited_search(nx, ny, new_vis, path + [(nx, ny)], limit)
        if result:
            return result
    return None

# Best-First Search
def best_first(start_x, start_y):
    initial_visited = [False]*64
    initial_visited[start_x*8 + start_y] = True
    heap = []
    heapq.heappush(heap, (0, 0, start_x, start_y, initial_visited, [(start_x, start_y)]))
    
    state_counter = 1
    
    while heap:
        _, count, x, y, visited, path = heapq.heappop(heap)
        current_level = len(path)
        print(f"Best-First: Processing state {count}")
        print_current_state(current_level, x, y, visited)
        
        if current_level == 64:
            return path
        
        for nx, ny, new_vis in get_successors(x, y, visited):
            priority = calculate_moves(nx, ny, new_vis)
            heapq.heappush(heap, (priority, state_counter, nx, ny, new_vis, path + [(nx, ny)]))
            state_counter += 1
    
    return None

# A* Search
def a_star(start_x, start_y):
    initial_visited = [False]*64
    initial_visited[start_x*8 + start_y] = True
    heap = []
    heapq.heappush(heap, (0 + calculate_moves(start_x, start_y, initial_visited), 
                         0, start_x, start_y, initial_visited, [(start_x, start_y)], 0))
    
    state_counter = 1
    
    while heap:
        _, count, x, y, visited, path, cost = heapq.heappop(heap)
        current_level = len(path)
        print(f"A*: Processing state {count}")
        print_current_state(current_level, x, y, visited)
        
        if current_level == 64:
            return path
        
        for nx, ny, new_vis in get_successors(x, y, visited):
            new_cost = cost + 1
            priority = new_cost + calculate_moves(nx, ny, new_vis)
            heapq.heappush(heap, (priority, state_counter, nx, ny, new_vis, 
                                 path + [(nx, ny)], new_cost))
            state_counter += 1
    
    return None

def print_solution(path):
    print("\nFinal Solution Path:")
    board = [[-1 for _ in range(8)] for _ in range(8)]
    for step, (x, y) in enumerate(path):
        board[x][y] = step
        print(f"Step {step}: ({x},{y})")
        for row in board:
            print(' '.join(f'{val:3d}' if val != -1 else '  .' for val in row))
        print()

def main():
    start_x, start_y = 0, 0
    
    print("\nStarting Best-First Search...")
    bfs_path = best_first(start_x, start_y)

    print("Starting Iterative Deepening Search...")
    ids_path = iterative_deepening(start_x, start_y)
    
    print("\nStarting A* Search...")
    astar_path = a_star(start_x, start_y)
    
    if ids_path:
        print_solution(ids_path)
    if bfs_path:
        print_solution(bfs_path)
    if astar_path:
        print_solution(astar_path)

if __name__ == "__main__":
    main()