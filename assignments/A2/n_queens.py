import pygame
import sys
import random
from collections import deque

# Color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

class FencesGame:
    def __init__(self, board_size=5, difficulty='easy'):
        self.board_size = board_size
        self.difficulty = difficulty
        self.cell_size = 60
        self.dot_radius = 5
        
        # Calculate grid dimensions
        self.red_rows = board_size
        self.blue_rows = board_size - 1
        self.width = (board_size * 2 - 1) * self.cell_size
        self.height = (board_size * 2 - 1) * self.cell_size
        
        # Initialize board structures
        self.red_h_fences = [[0]*(board_size-1) for _ in range(board_size)]
        self.red_v_fences = [[0]*board_size for _ in range(board_size-1)]
        self.blue_h_fences = [[0]*board_size for _ in range(board_size-1)]
        self.blue_v_fences = [[0]*(board_size-1) for _ in range(board_size)]
        
        # Initialize pre-built fences
        self._init_prebuilt_fences()
        
        self.current_player = 'human'  # human or computer
        self.game_over = False

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fences Game")

    def _init_prebuilt_fences(self):
        # Pre-build red top and bottom fences
        for col in range(self.board_size-1):
            self.red_h_fences[0][col] = 1
            self.red_h_fences[-1][col] = 1
        
        # Pre-build blue left and right fences
        for row in range(self.board_size-1):
            self.blue_v_fences[row][0] = 1
            self.blue_v_fences[row][-1] = 1

    def get_red_pos(self, row, col):
        x = (col * 2) * self.cell_size
        y = (row * 2) * self.cell_size
        return (x, y)

    def get_blue_pos(self, row, col):
        x = (col * 2 + 1) * self.cell_size
        y = (row * 2 + 1) * self.cell_size
        return (x, y)

    def is_red_h_fence_valid(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size-1

    def is_red_v_fence_valid(self, row, col):
        return 0 <= row < self.board_size-1 and 0 <= col < self.board_size

    def is_blue_h_fence_valid(self, row, col):
        return 0 <= row < self.board_size-1 and 0 <= col < self.board_size

    def is_blue_v_fence_valid(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size-1

    def place_red_fence(self, row, col, is_horizontal):
        if is_horizontal and self.is_red_h_fence_valid(row, col):
            if self.red_h_fences[row][col] == 0:
                self.red_h_fences[row][col] = 1
                return True
        elif not is_horizontal and self.is_red_v_fence_valid(row, col):
            if self.red_v_fences[row][col] == 0:
                self.red_v_fences[row][col] = 1
                return True
        return False

    def place_blue_fence(self, row, col, is_horizontal):
        if is_horizontal and self.is_blue_h_fence_valid(row, col):
            if self.blue_h_fences[row][col] == 0:
                self.blue_h_fences[row][col] = 1
                return True
        elif not is_horizontal and self.is_blue_v_fence_valid(row, col):
            if self.blue_v_fences[row][col] == 0:
                self.blue_v_fences[row][col] = 1
                return True
        return False

    def check_red_victory(self):
        # Check if red has connected top to bottom
        visited = [[False]*self.board_size for _ in range(self.board_size)]
        q = deque()

        # Start from top row
        for col in range(self.board_size):
            if self.red_h_fences[0][col] == 1:
                q.append((0, col))
                visited[0][col] = True

        while q:
            row, col = q.popleft()
            if row == self.board_size - 1:
                return True

            # Check all possible red connections
            # Right
            if col < self.board_size-1 and self.red_h_fences[row][col] == 1:
                if not visited[row][col+1]:
                    visited[row][col+1] = True
                    q.append((row, col+1))
            # Left
            if col > 0 and self.red_h_fences[row][col-1] == 1:
                if not visited[row][col-1]:
                    visited[row][col-1] = True
                    q.append((row, col-1))
            # Down
            if row < self.board_size-1 and self.red_v_fences[row][col] == 1:
                if not visited[row+1][col]:
                    visited[row+1][col] = True
                    q.append((row+1, col))
            # Up
            if row > 0 and self.red_v_fences[row-1][col] == 1:
                if not visited[row-1][col]:
                    visited[row-1][col] = True
                    q.append((row-1, col))
        return False

    def check_blue_victory(self):
        # Check if blue has connected left to right
        visited = [[False]*self.board_size for _ in range(self.board_size)]
        q = deque()

        # Start from left column
        for row in range(self.board_size-1):
            if self.blue_v_fences[row][0] == 1:
                q.append((row, 0))
                visited[row][0] = True

        while q:
            row, col = q.popleft()
            if col == self.board_size - 1:
                return True

            # Check all possible blue connections
            # Right
            if col < self.board_size-1 and self.blue_v_fences[row][col] == 1:
                if not visited[row][col+1]:
                    visited[row][col+1] = True
                    q.append((row, col+1))
            # Left
            if col > 0 and self.blue_v_fences[row][col-1] == 1:
                if not visited[row][col-1]:
                    visited[row][col-1] = True
                    q.append((row, col-1))
            # Down
            if row < self.board_size-2 and self.blue_h_fences[row][col] == 1:
                if not visited[row+1][col]:
                    visited[row+1][col] = True
                    q.append((row+1, col))
            # Up
            if row > 0 and self.blue_h_fences[row-1][col] == 1:
                if not visited[row-1][col]:
                    visited[row-1][col] = True
                    q.append((row-1, col))
        return False

    def get_available_blue_moves(self):
        moves = []
        # Check horizontal blue fences
        for row in range(len(self.blue_h_fences)):
            for col in range(len(self.blue_h_fences[row])):
                if self.blue_h_fences[row][col] == 0:
                    moves.append(('h', row, col))
        # Check vertical blue fences
        for row in range(len(self.blue_v_fences)):
            for col in range(len(self.blue_v_fences[row])):
                if self.blue_v_fences[row][col] == 0:
                    moves.append(('v', row, col))
        return moves

    def ai_move_easy(self):
        moves = self.get_available_blue_moves()
        return random.choice(moves) if moves else None

    def ai_move_hard(self):
        moves = self.get_available_blue_moves()
        # Prioritize moves that block potential red paths
        if moves:
            return random.choice(moves[:len(moves)//2])
        return None

    def draw_dots(self):
        # Draw red dots
        for row in range(self.red_rows):
            for col in range(self.board_size):
                x, y = self.get_red_pos(row, col)
                pygame.draw.circle(self.screen, RED, (x, y), self.dot_radius)

        # Draw blue dots
        for row in range(self.blue_rows):
            for col in range(self.board_size + 1):
                x, y = self.get_blue_pos(row, col)
                pygame.draw.circle(self.screen, BLUE, (x, y), self.dot_radius)

    def draw_fences(self):
        # Draw red horizontal fences
        for row in range(len(self.red_h_fences)):
            for col in range(len(self.red_h_fences[row])):
                if self.red_h_fences[row][col] == 1:
                    start = self.get_red_pos(row, col)
                    end = self.get_red_pos(row, col+1)
                    pygame.draw.line(self.screen, RED, start, end, 3)

        # Draw red vertical fences
        for row in range(len(self.red_v_fences)):
            for col in range(len(self.red_v_fences[row])):
                if self.red_v_fences[row][col] == 1:
                    start = self.get_red_pos(row, col)
                    end = self.get_red_pos(row+1, col)
                    pygame.draw.line(self.screen, RED, start, end, 3)

        # Draw blue horizontal fences
        for row in range(len(self.blue_h_fences)):
            for col in range(len(self.blue_h_fences[row])):
                if self.blue_h_fences[row][col] == 1:
                    start = self.get_blue_pos(row, col)
                    end = self.get_blue_pos(row, col+1)
                    pygame.draw.line(self.screen, BLUE, start, end, 3)

        # Draw blue vertical fences
        for row in range(len(self.blue_v_fences)):
            for col in range(len(self.blue_v_fences[row])):
                if self.blue_v_fences[row][col] == 1:
                    start = self.get_blue_pos(row, col)
                    end = self.get_blue_pos(row+1, col)
                    pygame.draw.line(self.screen, BLUE, start, end, 3)

    def handle_click(self, pos):
        x, y = pos
        for row in range(self.red_rows):
            for col in range(self.board_size):
                rx, ry = self.get_red_pos(row, col)
                if abs(x - rx) < 15 and abs(y - ry) < 15:
                    # Check horizontal fence to the right
                    if col < self.board_size - 1 and abs(x - (rx + self.cell_size*2)) < 20:
                        if self.place_red_fence(row, col, True):
                            return True
                    # Check vertical fence below
                    if row < self.red_rows - 1 and abs(y - (ry + self.cell_size*2)) < 20:
                        if self.place_red_fence(row, col, False):
                            return True
        return False

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.current_player == 'human':
                    if self.handle_click(event.pos):
                        if self.check_red_victory():
                            print("Human wins!")
                            self.game_over = True
                        self.current_player = 'computer'

            if self.current_player == 'computer' and not self.game_over:
                move = self.ai_move_easy() if self.difficulty == 'easy' else self.ai_move_hard()
                if move:
                    fence_type, row, col = move
                    if fence_type == 'h':
                        self.place_blue_fence(row, col, True)
                    else:
                        self.place_blue_fence(row, col, False)
                    
                    if self.check_blue_victory():
                        print("Computer wins!")
                        self.game_over = True
                    self.current_player = 'human'

            self.screen.fill(WHITE)
            self.draw_dots()
            self.draw_fences()
            pygame.display.flip()

if __name__ == "__main__":
    while True:
        difficulty = input("Enter difficulty level (easy/hard): ").strip().lower()
        if difficulty in ['easy', 'hard']:
            break
        print("Invalid input. Please enter 'easy' or 'hard'.")
    if difficulty == 'easy':
        game = FencesGame(board_size=5, difficulty=difficulty)
    else:   
        game = FencesGame(board_size=8, difficulty=difficulty) 
    game.run()