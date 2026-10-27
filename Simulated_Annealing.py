import random
import math

# Define the Environment class
class Environment:
    def __init__(self):
        # Randomly place 8 queens, one in each column
        self.board = [random.randint(0, 7) for _ in range(8)]


# Define the Simulated Annealing Agent class
class SimulatedAnnealingAgent:
    def __init__(self, environment):
        self.board = environment.board[:]

    # Calculate the number of attacking pairs of queens
    def cost(self, board):
        conflicts = 0

        for i in range(8):
            for j in range(i + 1, 8):
                if (board[i] == board[j] or
                    abs(board[i] - board[j]) == abs(i - j)):
                    conflicts += 1

        return conflicts

    # Perform Simulated Annealing
    def solve(self, max_restarts=100, initial_temperature=100,
              cooling_rate=0.99, max_iterations=5000):

        for restart in range(max_restarts):
            # Generate a new random board for each restart
            self.board = [random.randint(0, 7) for _ in range(8)]
            temperature = initial_temperature

            for iteration in range(max_iterations):
                current_cost = self.cost(self.board)

                # Stop if a valid solution is found
                if current_cost == 0:
                    print("\nSolution Found!")
                    print("Number of restarts:", restart)
                    print("Iterations:", iteration)
                    self.printBoard()
                    self.printPositions()
                    print("Cost:", self.cost(self.board))
                    return True

                # Generate a neighboring board by moving one queen
                next_board = self.board[:]
                col = random.randint(0, 7)

                # Choose a different row for the selected queen
                possible_rows = [
                    row for row in range(8)
                    if row != next_board[col]
                ]
                next_board[col] = random.choice(possible_rows)

                next_cost = self.cost(next_board)

                # Calculate energy change
                delta_e = current_cost - next_cost

                # Accept better moves; sometimes accept worse moves
                if delta_e > 0:
                    self.board = next_board
                else:
                    probability = math.exp(delta_e / temperature)

                    if random.random() < probability:
                        self.board = next_board

                # Cool the temperature
                temperature *= cooling_rate

                # Prevent temperature from becoming too small
                if temperature < 0.001:
                    break

        print("\nSolution not found after maximum restarts.")
        print("Try increasing max_restarts or max_iterations.")
        return False

    # Display the chessboard
    def printBoard(self):
        print("\nChessboard:")
        for row in range(8):
            for col in range(8):
                if self.board[col] == row:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

    # Display queen positions using 1-based indexing
    def printPositions(self):
        print("\nQueen positions (Column, Row):")
        for col, row in enumerate(self.board):
            print(f"Queen {col + 1}: Column {col + 1}, Row {row + 1}")


# Main program
if __name__ == "__main__":
    environment = Environment()
    agent = SimulatedAnnealingAgent(environment)
    agent.solve()