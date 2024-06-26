import pygame
import sys
import time

import tictactoe2 as ttt

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.SysFont("Arial", 28)
largeFont = pygame.font.SysFont("Arial", 40)
moveFont = pygame.font.SysFont("Arial", 60)

user = None
board = ttt.initial_state()
ai_turn = False


def draw_title(title_text):
    title = largeFont.render(title_text, True, white)
    titleRect = title.get_rect()
    titleRect.center = ((width / 2), 50)
    screen.blit(title, titleRect)


def draw_button(text, rect):
    button_text = mediumFont.render(text, True, black)
    button_rect = button_text.get_rect()
    button_rect.center = rect.center
    pygame.draw.rect(screen, white, rect)
    screen.blit(button_text, button_rect)


def draw_board():
    tile_size = 80
    tile_origin = (width / 2 - (1.5 * tile_size), height / 2 - (1.5 * tile_size))
    tiles = []
    for i in range(3):
        row = []
        for j in range(3):
            rect = pygame.Rect(
                tile_origin[0] + j * tile_size,
                tile_origin[1] + i * tile_size,
                tile_size, tile_size
            )
            pygame.draw.rect(screen, white, rect, 3)

            if board[i][j] != ttt.EMPTY:
                move = moveFont.render(board[i][j], True, white)
                moveRect = move.get_rect()
                moveRect.center = rect.center
                screen.blit(move, moveRect)
            row.append(rect)
        tiles.append(row)
    return tiles


def handle_user_click(mouse, tiles):
    global board
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                board = ttt.result(board, (i, j))
                return True
    return False


def main():
    global user, board, ai_turn
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if user is None:
                    if playXButton.collidepoint(mouse):
                        time.sleep(0.2)
                        user = ttt.X
                    elif playOButton.collidepoint(mouse):
                        time.sleep(0.2)
                        user = ttt.O
                else:
                    if user == ttt.player(board) and not ttt.terminal(board):
                        if handle_user_click(mouse, tiles):
                            ai_turn = True
                    elif ttt.terminal(board) and againButton.collidepoint(mouse):
                        time.sleep(0.2)
                        user = None
                        board = ttt.initial_state()
                        ai_turn = False

        screen.fill(black)

        if user is None:
            draw_title("Play Tic-Tac-Toe")
            draw_button("Play as X", playXButton)
            draw_button("Play as O", playOButton)
        else:
            tiles = draw_board()
            game_over = ttt.terminal(board)
            player = ttt.player(board)

            if game_over:
                winner = ttt.winner(board)
                title_text = f"Game Over: {winner} wins." if winner else "Game Over: Tie."
            elif user == player:
                title_text = f"Play as {user}"
            else:
                title_text = "Computer thinking..."
            draw_title(title_text)

            if user != player and not game_over and ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False

            if game_over:
                draw_button("Play Again", againButton)

        pygame.display.flip()


playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)

if __name__ == "__main__":
    main()
