import random
class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(self, player):
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],  
            [self.board[1][0], self.board[1][1], self.board[1][2]],  
            [self.board[2][0], self.board[2][1], self.board[2][2]],  
            [self.board[0][0], self.board[1][0], self.board[2][0]],  
            [self.board[0][1], self.board[1][1], self.board[2][1]],  
            [self.board[0][2], self.board[1][2], self.board[2][2]],  
            [self.board[0][0], self.board[1][1], self.board[2][2]],  # Diagonal from top-left
            [self.board[2][0], self.board[1][1], self.board[0][2]],  # Diagonal from bottom-left
        ]
        return [player, player, player] in win_conditions

    def get_available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    moves.append((i, j))
        return moves

    def make_move(self, move, player):
        self.board[move[0]][move[1]] = player

    def get_random_move(self):
        moves = self.get_available_moves()
        return random.choice(moves)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        while True:
            self.print_board()
            if self.current_player == "X":
                # Human player's move
                row = int(input("Enter the row (0, 1, 2): "))
                col = int(input("Enter the column (0, 1, 2): "))
                if (row, col) not in self.get_available_moves():
                    print("Invalid move. Try again.")
                    continue
                self.make_move((row, col), self.current_player)
            else:
                # AI's move
                print("AI is making a move...")
                move = self.get_random_move()
                self.make_move(move, self.current_player)

            # Check for a winner
            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            # Check for a tie
            if not self.get_available_moves():
                self.print_board()
                print("It's a tie!")
                break

            # Switch players
            self.switch_player()

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
