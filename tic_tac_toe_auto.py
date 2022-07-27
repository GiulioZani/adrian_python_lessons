# autopilot tic tac toe example

# implements a game tic tac toe

# imports
import random

# creates a game class for tic tac toe.
class TicTacToe:
    # initializes the game
    def __init__(self):
        # initialize the board
        self.board = [" "] * 10
        # initialize the player
        self.player = "X"
        # initialize the computer
        self.computer = "O"
        # initialize the game status
        self.game_status = True
        # initialize the winner
        self.winner = None
        # initialize the move counter
        self.move_counter = 0
        # initialize the tie
        self.tie = False
        # initialize the move
        self.move = 0
        # initialize the computer move
        self.computer_move = 0
        
    # prints the board
    def print_board(self):
        # print the board
        print("\n")
        # print the top row
        print("   |   |   ")
        # print the middle row
        print(" " + self.board[7] + " | " + self.board[8] + " | " + self.board[9])
        # print the bottom row
        print("   |   |   ")
        # print the separator
        print("-----------")
    
    #checks if the game is over
    def is_game_over(self):
        # check if the game is over
        if self.winner is not None:
            # game is over
            self.game_status = False
        elif self.move_counter == 9:
            self.game_status = 'draw'
        else:
            self.game_status = True
        # return the game status
        return self.game_status
    
    # checks if the player has won
    def is_player_won(self):
        # check if the player has won
        if self.board[7] == self.player and self.board[8] == self.player and self.board[9] == self.player:
            # player has won
            self.winner = self.player
        elif self.board[4] == self.player and self.board[5] == self.player and self.board[6] == self.player:
            # player has won
            self.winner = self.player
        elif self.board[1] == self.player and self.board[2] == self.player and self.board[3] == self.player:
            # player has won
            self.winner = self.player
        elif self.board[7] == self.player and self.board[4] == self.player and self.board[1] == self.player:
            # player has won
            self.winner = self.player
        elif self.board[8] == self.player and self.board[5] == self.player and self.board[2] == self.player:
            # player has won
            self.winner = self.player
        elif self.board[9] == self.player and self.board[6] == self.player and self.board[3] == self.player:
            # player has won
            self.winner = self.player
        elif self.board[7] == self.player and self.board[5] == self.player and self.board[3] == self.player:
            # player has won
            self.winner = self.player
        elif self.board[9] == self.player and self.board[5] == self.player and self.board[1] == self.player:
            # player has won
            self.winner = self.player
        else:
            # player has not won
            self.winner = None
        # return the winner
        return self.winner

# checks if the computer has won
    def is_computer_won(self):
        # check if the computer has won
        if self.board[7] == self.computer and self.board[8] == self.computer and self.board[9] == self.computer:
            # computer has won
            self.winner = self.computer
        elif self.board[4] == self.computer and self.board[5] == self.computer and self.board[6] == self.computer:
            # computer has won
            self.winner = self.computer
        elif self.board[1] == self.computer and self.board[2] == self.computer and self.board[3] == self.computer:
            # computer has won
            self.winner = self.computer
        elif self.board[7] == self.computer and self.board[4] == self.computer and self.board[1] == self.computer:
            # computer has won
            self.winner = self.computer
        elif self.board[8] == self.computer and self.board[5] == self.computer and self.board[2] == self.computer:
            # computer has won
            self.winner = self.computer
        elif self.board[9] == self.computer and self.board[6] == self.computer and self.board[3] == self.computer:
            # computer has won
            self.winner = self.computer
        elif self.board[7] == self.computer and self.board[5] == self.computer and self.board[3] == self.computer:
            # computer has won
            self.winner = self.computer
        elif self.board[9] == self.computer and self.board[5] == self.computer and self.board[1] == self.computer:
            # computer has won
            self.winner = self.computer
        else:
            # computer has not won
            self.winner = None
        # return the winner
        return self.winner

# checks if the game is a tie
    def is_tie(self):
        # check if the game is a tie
        if self.move_counter == 9:
            # game is a tie
            self.tie = True
        else:
            # game is not a tie
            self.tie = False
        # return the tie
        return self.tie

# check if the move is valid
    def is_move_valid(self, move):
        # check if the move is valid
        if move in range(1, 10) and self.board[move] == " ":
            # move is valid
            return True
        else:
            # move is not valid
            return False

# makes the move
    def make_move(self, move, player):
        # make the move
        self.board[move] = player
        # update the move counter
        self.move_counter += 1
        # update the board
        self.print_board()
        # update the winner
        self.winner = self.is_player_won()
        # update the winner
        self.winner = self.is_computer_won()
        # update the game status
        self.is_game_over()
        # update the tie
        self.tie = self.is_tie()

    def run(self):
    # run the game
        while self.game_status:
            # check if the game is over
            if self.is_game_over() == 'draw':
                # game is a tie
                print("The game is a tie!")
                break
            elif self.is_game_over() == False:
                # game is over
                print("The game is over!")
                break
            # check if the player has won
            if self.winner == self.player:
                # player has won
                print("The player has won!")
                break
            # check if the computer has won
            elif self.winner == self.computer:
                # computer has won
                print("The computer has won!")
                break
            # check if the game is a tie
            elif self.tie:
                # game is a tie
                print("The game is a tie!")
                break
                # ask the player to make a move
                move = int(input("Enter your move: "))
            # check if the move is valid
            if self.is_move_valid(move):
                # make the move
                self.make_move(move, self.player)
            # check if the game is over
            if self.is_game_over() == 'draw':
                # game is a tie
                print("The game is a tie!")
                break
            elif self.is_game_over() == False:
                # game is over
                print("The game is over!")
                break
            # check if the player has won
            if self.winner == self.player:
                # player has won
                print("The player has won!")
                break
            # check if the computer has won
            elif self.winner == self.computer:
                # computer has won
                print("The computer has won!")
                break
            # check if the game is a tie
            elif self.tie:
                # game is a tie
                print("The game is a tie!")
                break
            # make the computer move
            self.make_move(self.computer_move(), self.computer)

# gets the move of the computer
    def computer_move(self):
        # check if the computer has won
        if self.is_computer_won():
            # computer has won
            return self.winner
        # check if the player has won
        elif self.is_player_won():
            # player has won
            return self.winner
        # check if the game is a tie
        elif self.is_tie():
            # game is a tie
            return self.tie
        # check if the computer has a winning move
        elif self.board[5] == self.computer:
            # computer has a winning move
            return 5
        elif self.board[1] == self.computer:
            # computer has a winning move
            return 1
        elif self.board[3] == self.computer:
            # computer has a winning move
            return 3
        elif self.board[7] == self.computer:
            # computer has a winning move
            return 7
        elif self.board[9] == self.computer:
            # computer has a winning move
            return 9
        elif self.board[2] == self.computer:
            # computer has a winning move
            return 2
        elif self.board[8] == self.computer:
            # computer has a winning move
            return 8
        elif self.board[6] == self.computer:
            # computer has a winning move
            return 6
        elif self.board[4] == self.computer:
            # computer has a winning move
            return 4
        # check if the computer has a blocking move
        elif self.board[5] == self.player:
            # computer has a blocking move
            return 5
        elif self.board[1] == self.player:
            # computer has a blocking move
            return 1
        elif self.board[3] == self.player:
            # computer has a blocking move
            return 3
        elif self.board[7] == self.player:
            # computer has a blocking move
            return 7
        elif self.board[9] == self.player:
            # computer has a blocking move
            return 9

# gets the move of the player
    def player_move(self):
        # check if the player has won
        if self.is_player_won():
            # player has won
            return self.winner
        # check if the computer has won
        elif self.is_computer_won():
            # computer has won
            return self.winner
        # check if the game is a tie
        elif self.is_tie():
            # game is a tie
            return self.tie
        # check if the player has a winning move
        elif self.board[5] == self.player:
            # player has a winning move
            return 5
        elif self.board[1] == self.player:
            # player has a winning move
            return 1
        elif self.board[3] == self.player:
            # player has a winning move
            return 3
        elif self.board[7] == self.player:
            # player has a winning move
            return 7
        elif self.board[9] == self.player:
            # player has a winning move
            return 9
        elif self.board[2] == self.player:
            # player has a winning move
            return 2
        elif self.board[8] == self.player:
            # player has a winning move
            return 8
        elif self.board[6] == self.player:
            # player has a winning move
            return 6
        elif self.board[4] == self.player:
            # player has a winning move
            return 4
        # check if the player has a blocking move
        elif self.board[5] == self.computer:
            # player has a blocking move
            return 5
        elif self.board[1] == self.computer:
            # player has a blocking move
            return 1
        elif self.board[3] == self.computer:
            # player has a blocking move
            return 3
        elif self.board[7] == self.computer:
            # player has a blocking move
            return 7
        elif self.board[9] == self.computer:
            # player has a blocking move
            return 9

# create the game
game = TicTacToe()

# run the game
if __name__ == '__main__':
    game.run()
