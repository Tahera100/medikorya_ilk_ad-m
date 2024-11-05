import pygame
import sys
import random
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Initialize pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer for music
block_size = 30  # Size of each block
grid_width, grid_height = 15, 20  # Grid size in blocks
font = pygame.font.SysFont("Arial", 24)

# Function to open file dialog and select music
def select_music():
    Tk().withdraw()  # Hide the root Tkinter window
    filename = askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    return filename

# Welcome screen
def welcome_screen():
    screen = pygame.display.set_mode((grid_width * block_size, grid_height * block_size))
    pygame.display.set_caption("Welcome to Tetris")
    input_box = pygame.Rect(50, 200, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    music_file = ''

    while True:
        screen.fill((0, 0, 0))
        welcome_text = font.render("Welcome to Tetris! :)", True, (255, 255, 255))
        instructions_text = font.render("Enter your name:", True, (255, 255, 255))
        upload_music_text = font.render("Press Enter to upload your music!", True, (255, 255, 255))
        screen.blit(welcome_text, (50, 50))
        screen.blit(instructions_text, (50, 100))
        screen.blit(upload_music_text, (50, 150))
        
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, input_box)
        pygame.draw.rect(screen, color, input_box, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if text:                          # Only if text is not empty
                        music_file = select_music()   # Open file dialog to select music
                        if music_file:                # If music file is selected
                            return text, music_file   # Return name and music file
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        pygame.display.flip()

# Tetris game implementation
def tetris_game(player_name, music_file):
    screen = pygame.display.set_mode((grid_width * block_size, grid_height * block_size))
    pygame.display.set_caption("Tetris")
    
    # Load and play background music
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    clock = pygame.time.Clock()

    # Colors and shapes
    colors = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (255, 165, 0), (0, 0, 255)]
    shapes = [
        [[1, 1, 1, 1]],                # I shape
        [[1, 1], [1, 1]],              # O shape
        [[1, 1, 1], [0, 1, 0]],        # T shape
        [[1, 1, 0], [0, 1, 1]],        # S shape
        [[0, 1, 1], [1, 1, 0]],        # Z shape
        [[1, 1, 1], [1, 0, 0]],        # L shape
        [[1, 1, 1], [0, 0, 1]]         # J shape
    ]

    # Game grid
    grid = [[(0, 0, 0) for _ in range(grid_width)] for _ in range(grid_height)]
    score = 0

    class Piece:
        def __init__(self, shape):
            self.shape = shape
            self.color = colors[shapes.index(shape)]
            self.x, self.y = 3, 0  # Starting position

        def draw(self, surface):
            for y, row in enumerate(self.shape):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(
                            surface,
                            self.color,
                            ((self.x + x) * block_size, (self.y + y) * block_size, block_size, block_size)
                        )

        def move(self, dx, dy):
            self.x += dx
            self.y += dy

    # Check collision function
    def check_collision(piece, dx, dy):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = piece.x + x + dx, piece.y + y + dy
                    if new_x < 0 or new_x >= grid_width or new_y >= grid_height or grid[new_y][new_x] != (0, 0, 0):
                        return True
        return False

    # Lock piece in grid
    def lock_piece(piece):
        global grid, score
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid[piece.y + y][piece.x + x] = piece.color

        # Check for full rows
        for y in range(grid_height):
            if all(grid[y][x] != (0, 0, 0) for x in range(grid_width)):
                del grid[y]
                grid.insert(0, [(0, 0, 0) for _ in range(grid_width)])
                score += 10

    # Display game-over message
    def game_over(surface):
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        player_score_text = font.render(f"{player_name}, your Score: {score}", True, (255, 255, 255))
        surface.blit(game_over_text, (surface.get_width() // 2 - 50, surface.get_height() // 2))
        surface.blit(player_score_text, (surface.get_width() // 2 - 100, surface.get_height() // 2 + 30))
        pygame.display.update()
        pygame.time.delay(2000)

    # Main game loop
    current_piece = Piece(random.choice(shapes))
    fall_time = 0

    while True:
        screen.fill((0, 0, 0))  # Background color (black)
        fall_time += clock.get_rawtime()
        clock.tick(10)

        # Move piece down automatically
        if fall_time / 1000 > 0.2:
            if not check_collision(current_piece, 0, 1):
                current_piece.move(0, 1)
            else:
                lock_piece(current_piece)
                current_piece = Piece(random.choice(shapes))
                if check_collision(current_piece, 0, 0):
                    game_over(screen)
                    pygame.quit()
                    sys.exit()
            fall_time = 0

        # Draw grid lines in white
        grid_line_color = (255, 255, 255)    # White color
        for x in range(grid_width + 1):      # Vertical lines
            pygame.draw.line(screen, grid_line_color, (x * block_size, 0), (x * block_size, grid_height * block_size))
        for y in range(grid_height + 1):     # Horizontal lines
            pygame.draw.line(screen, grid_line_color, (0, y * block_size), (grid_width * block_size, y * block_size))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(current_piece, -1, 0):
                    current_piece.move(-1, 0)
                elif event.key == pygame.K_RIGHT and not check_collision(current_piece, 1, 0):
                    current_piece.move(1, 0)
                elif event.key == pygame.K_DOWN and not check_collision(current_piece, 0, 1):
                    current_piece.move(0, 1)

        # Draw grid and piece
        for y in range(grid_height):
            for x in range(grid_width):
                pygame.draw.rect(screen, grid[y][x], (x * block_size, y * block_size, block_size, block_size))
        current_piece.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

# Main program execution
if __name__ == "__main__":
    player_name, music_file = welcome_screen()  # Get player name and music file
    tetris_game(player_name, music_file) 
