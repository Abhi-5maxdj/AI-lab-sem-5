#Implementation of Tic-Tac-Toe using a simple agent in Python

# Define the environment class
class Environment:
    def __init__(self):
        # Initialize the Tic-Tac-Toe board
        self.board = [' ' for _ in range(9)]


# Define the Tic-Tac-Toe agent class
class SimpleTicTacToeAgent:
    def __init__(self, environment):

        # Print the initial board
        self.printBoard(environment)

        while True:
            # Human player move
            move = int(input("Enter your position (1-9): ")) - 1

            if move < 0 or move > 8 or environment.board[move] != ' ':
                print("Invalid move!")
                continue

            environment.board[move] = 'X'

            self.printBoard(environment)

            # Check if human won
            if self.checkWinner(environment, 'X'):
                print("You Win!")
                break

            # Check for draw
            if self.isFull(environment):
                print("Draw!")
                break

            # Agent's move
            print("Agent is making a move...")

            # Agent chooses center if available
            if environment.board[4] == ' ':
                environment.board[4] = 'O'

            # Otherwise choose the first empty position
            else:
                for i in range(9):
                    if environment.board[i] == ' ':
                        environment.board[i] = 'O'
                        break

            self.printBoard(environment)

            # Check if agent won
            if self.checkWinner(environment, 'O'):
                print("Agent Wins!")
                break

            # Check for draw
            if self.isFull(environment):
                print("Draw!")
                break

    # Function to print the board
    def printBoard(self, environment):
        board = environment.board

        print()
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])
        print()

    # Function to check winner
    def checkWinner(self, environment, player):

        winningPositions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winningPositions:
            if environment.board[a] == player and \
               environment.board[b] == player and \
               environment.board[c] == player:
                return True

        return False

    # Function to check if board is full
    def isFull(self, environment):
        return ' ' not in environment.board


# Create an instance of the Environment class
theEnvironment = Environment()

# Create an instance of the Tic-Tac-Toe agent
theAgent = SimpleTicTacToeAgent(theEnvironment)