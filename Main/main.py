import pygame
import sys
import chess

# Inicijalizacija Pygame-a
pygame.init()

# Postavke prozora
WIDTH, HEIGHT = 900, 1000
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
BOARD_COLOR = (150, 75, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (128, 128, 0)
RED = (211, 47, 47)
BLUE = (21, 101, 192)
BROWN = (139, 69, 19)
PURPLE = (52, 32, 72)
CHECK_COLOR = (211, 47, 47)
CHECKMATE_COLOR = (255, 0, 0)
FONT = pygame.font.Font(None, 36)

# dimenzije ploče
board_width = BOARD_SIZE * SQUARE_SIZE
board_height = BOARD_SIZE * SQUARE_SIZE
# centriranje ploče
board_x = (WIDTH - board_width) // 2
board_y = (HEIGHT - board_height) // 2

# Postavljanje prozora
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Šah by Faruk")

# Varijabla za praćenje stanja igre
game_state = "MENU"
draggable = False  # Varijabla za praćenje je li figura povučena

# Funkcija za crtanje 'start menu'
def draw_menu():
    screen.fill(BLACK) # boja pozadine
    start_text = FONT.render("Start", True, WHITE)
    exit_text = FONT.render("Exit", True, WHITE)
    restart_text = FONT.render("Restart", True, WHITE)

    # gumb "Start i "Exit"
    pygame.draw.rect(screen, BLUE, (WIDTH // 2 - 50, HEIGHT // 2 - 50, 100, 50))
    pygame.draw.rect(screen, RED, (WIDTH // 2 - 50, HEIGHT // 2, 100, 50))
    pygame.draw.rect(screen, PURPLE, (WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50))

    # text na gumbu
    screen.blit(start_text, (WIDTH // 2 - 30, HEIGHT // 2 - 40))
    screen.blit(exit_text, (WIDTH // 2 - 30, HEIGHT // 2 + 10))
    screen.blit(restart_text, (WIDTH // 2 - 30, HEIGHT // 2 + 60))

# Učitavanje slika figura
white_rook = pygame.image.load("white_rook.png")
white_knight = pygame.image.load("white_knight.png")
white_bishop = pygame.image.load("white_bishop.png")
white_queen = pygame.image.load("white_queen.png")
white_king = pygame.image.load("white_king.png")
white_pawn = pygame.image.load("white_pawn.png")
black_rook = pygame.image.load("black_rook.png")
black_knight = pygame.image.load("black_knight.png")
black_bishop = pygame.image.load("black_bishop.png")
black_queen = pygame.image.load("black_queen.png")
black_king = pygame.image.load("black_king.png")
black_pawn = pygame.image.load("black_pawn.png")

# Inicijalizacija šahovske ploče
board = chess.Board()

# Funkcija za crtanje šahovske ploče
def draw_board():
    # Smeđi stol
    pygame.draw.rect(screen, BROWN, (0, 0, WIDTH, HEIGHT))

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, WHITE, (board_x + col * SQUARE_SIZE, board_y + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (board_x + col * SQUARE_SIZE, board_y + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Funkcija za crtanje figura na ploči
def draw_pieces() -> object:
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece is not None:
                x = board_x + col * SQUARE_SIZE + SQUARE_SIZE // 2
                y = board_y + row * SQUARE_SIZE + SQUARE_SIZE // 2
                if piece.color == chess.WHITE:
                    if piece.piece_type == chess.PAWN:
                        screen.blit(white_pawn, (x - 32, y - 32))
                    elif piece.piece_type == chess.ROOK:
                        screen.blit(white_rook, (x - 32, y - 32))
                    elif piece.piece_type == chess.KNIGHT:
                        screen.blit(white_knight, (x - 32, y - 32))
                    elif piece.piece_type == chess.BISHOP:
                        screen.blit(white_bishop, (x - 32, y - 32))
                    elif piece.piece_type == chess.QUEEN:
                        screen.blit(white_queen, (x - 32, y - 32))
                    elif piece.piece_type == chess.KING:
                        screen.blit(white_king, (x - 32, y - 32))
                    # bijele figure ^^^^
                if piece.color == chess.BLACK:
                    if piece.piece_type == chess.PAWN:
                        screen.blit(black_pawn, (x - 32, y - 32))
                    elif piece.piece_type == chess.ROOK:
                        screen.blit(black_rook, (x - 32, y - 32))
                    elif piece.piece_type == chess.KNIGHT:
                        screen.blit(black_knight, (x - 32, y - 32))
                    elif piece.piece_type == chess.BISHOP:
                        screen.blit(black_bishop, (x - 32, y - 32))
                    elif piece.piece_type == chess.QUEEN:
                        screen.blit(black_queen, (x - 32, y - 32))
                    elif piece.piece_type == chess.KING:
                        screen.blit(black_king, (x - 32, y - 32))
                    # crne figure ^^^^

# Glavna petlja igre
running = True
selected_square = None  # Varijabla za praćenje odabrane figure

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Implementirajte logiku za poteze igrača na temelju klika mišem
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_col = (mouse_x - board_x) // SQUARE_SIZE
            clicked_row = (mouse_y - board_y) // SQUARE_SIZE

            if game_state == "MENU":
                # Provjera klika
                if WIDTH // 2 - 50 <= mouse_x <= WIDTH // 2 + 50:
                    if HEIGHT // 2 - 50 <= mouse_y <= HEIGHT // 2 - 50 + 50:
                        game_state = "PLAY"
                    elif HEIGHT // 2 <= mouse_y <= HEIGHT // 2 + 50:
                        running = False
                    elif HEIGHT // 2 + 100 <= mouse_y <= HEIGHT // 2 + 100 + 50:
                        # resetuje igru
                        board = chess.Board()
                        game_state = "PLAY"
                        draggable = False
                        selected_square = None
            elif game_state == "PLAY":
                if WIDTH - 100 <= mouse_x <= WIDTH and 0 <= mouse_y <= 50:
                    game_state = "MENU"
                if 0 <= clicked_col < BOARD_SIZE and 0 <= clicked_row < BOARD_SIZE:
                    square = chess.square(clicked_col, 7 - clicked_row)  # Obrnemo redoslijed za šahovsku ploču
                    piece = board.piece_at(square)

                    if draggable:
                        # Pokušaj napraviti potez ako je figura povučena
                        move = chess.Move(selected_square, square)
                        if move in board.legal_moves:
                            # Potez je ispravan, ažuriraj ploču
                            board.push(move)
                        selected_square = None
                        draggable = False
                    elif piece is not None:
                        # Ako ima figure na odabranom polju, označi je kao povučenu
                        selected_square = square
                        draggable = True


    status_message = "PLAYING"
    status_color = GREEN

    if game_state == "MENU":
        draw_menu()
        status_message = "IN MENU"
        status_color = GREEN
        status_text = FONT.render(f"Status: {status_message}", True, status_color)
        screen.blit(status_text, (10, 10))

    elif game_state == "PLAY":
        screen.fill(BOARD_COLOR)
        pygame.draw.rect(screen, BROWN, (0, 0, WIDTH, HEIGHT))
        draw_board()
        draw_pieces()

    # Implementirajte logiku za provjeru statusa igre (check/checkmate)
    if board.is_check():
        status_message = "CHECK"
        status_color = RED
    status_text = FONT.render(f"Status: {status_message}", True, status_color)
    screen.blit(status_text, (10, 10))

    if board.is_checkmate():
        status_message = "CHECKMATE"
        status_color = BLUE
        status_text = FONT.render(f"Status: {status_message}", True, status_color)
        screen.blit(status_text, (10, 10))

    # Prikaz gumba za izlaz na početak
    pygame.draw.rect(screen, (0, 255, 0, 128), (WIDTH - 100, 0, 100, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()


