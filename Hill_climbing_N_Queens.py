# Implementation of Hill Climbing for N-Queens Problem

import random

# Define the environment class
class Environment:
    def __init__(self, n):
        self.n = n

        # Place one queen randomly in each column
        self.board = [random.randint(0, n - 1) for _ in range(n)]


# Define the Hill Climbing agent class
class HillClimbingAgent:
    def __init__(self, environment):
        self.environment = environment
        self.n = environment.n

        # Start with the initial board
        self.board = environment.board

        print("Initial Board:")
        self.printBoard()

        # Perform Hill Climbing
        while True:
            currentHeuristic = self.heuristic(self.board)

            # Solution found
            if currentHeuristic == 0:
                print("Solution Found!")
                break

            bestBoard = self.board.copy()
            bestHeuristic = currentHeuristic

            # Try moving each queen to another row
            for col in range(self.n):
                for row in range(self.n):
                    if row != self.board[col]:
                        newBoard = self.board.copy()
                        newBoard[col] = row

                        h = self.heuristic(newBoard)

                        if h < bestHeuristic:
                            bestHeuristic = h
                            bestBoard = newBoard

            # Stop if no better state is found
            if bestHeuristic >= currentHeuristic:
                print("Local maximum reached. No solution found.")
                break

            self.board = bestBoard

        print("\nFinal Board:")
        self.printBoard()
        print("Heuristic:", self.heuristic(self.board))

    # Count pairs of queens attacking each other
    def heuristic(self, board):
        conflicts = 0

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if board[i] == board[j] or \
                   abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1

        return conflicts

    # Display the board
    def printBoard(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.board[col] == row:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()


# Main program
n = int(input("Enter the number of queens: "))

theEnvironment = Environment(n)
theAgent = HillClimbingAgent(theEnvironment)