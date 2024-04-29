import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 300, 300
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
BG_COLOR = (200, 200, 200)
LINE_WIDTH = 4
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize game variables
board = [['' for _ in range(COLS)] for _ in range(ROWS)]
player_turn = 'X'
game_over = False

# Function to draw the grid lines
def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(win, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    for i in range(1, COLS):
        pygame.draw.line(win, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw X's and O's on the board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 'X':
                pygame.draw.line(win, LINE_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE), ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
                pygame.draw.line(win, LINE_COLOR, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE), (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(win, LINE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - LINE_WIDTH, LINE_WIDTH)

# Function to check if a player has won
def check_win(player):
    for row in range(ROWS):
        if all(board[row][col] == player for col in range(COLS)):
            return True
    for col in range(COLS):
        if all(board[row][col] == player for row in range(ROWS)):
            return True
    if all(board[i][i] == player for i in range(ROWS)):
        return True
    if all(board[i][ROWS - i - 1] == player for i in range(ROWS)):
        return True
    return False

# Main game loop
while not game_over:
    win.fill(BG_COLOR)
    draw_grid()
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = player_turn
                if check_win(player_turn):
                    print(f'{player_turn} wins!')
                    game_over = True
                elif all(board[i][j] != '' for i in range(ROWS) for j in range(COLS)):
                    print("It's a draw!")
                    game_over = True
                else:
                    player_turn = 'O' if player_turn == 'X' else 'X'

    pygame.display.update()
