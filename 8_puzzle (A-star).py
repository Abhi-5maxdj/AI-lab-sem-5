# Implementation of 8-Puzzle using A* Search in Python

# Define the environment class
class Environment:
    def __init__(self):

        # Initial state
        self.initialState = [1, 2, 3,
                             4, 0, 6,
                             7, 5, 8]

        # Goal state
        self.goalState = [1, 2, 3,
                          4, 5, 6,
                          7, 8, 0]


# Define the A* agent class
class AStarAgent:
    def __init__(self, environment, heuristic):

        self.environment = environment
        self.heuristic = heuristic

        print("Initial State:")
        self.printState(environment.initialState)

        self.aStar()

    # A* Search
    def aStar(self):

        initial = self.environment.initialState
        goal = self.environment.goalState

        # Open list contains:
        # (f, g, state, path)
        openList = []

        # Add initial state
        g = 0
        h = self.calculateHeuristic(initial)
        f = g + h

        openList.append((f, g, initial, [initial]))

        # Store visited states
        visited = set()

        while openList:

            # Find state with minimum f value
            openList.sort(key=lambda x: x[0])

            f, g, state, path = openList.pop(0)

            stateTuple = tuple(state)

            # Skip already visited states
            if stateTuple in visited:
                continue

            visited.add(stateTuple)

            # Check if goal is reached
            if state == goal:

                print("Goal State Reached!")
                print("Cost:", g)

                print("\nSolution Path:")

                for s in path:
                    self.printState(s)

                return

            # Find blank tile
            blankPosition = state.index(0)

            row = blankPosition // 3
            col = blankPosition % 3

            # Possible moves
            moves = [
                (-1, 0), # Up
                (1, 0), # Down
                (0, -1), # Left
                (0, 1) # Right
            ]

            # Generate successors
            for dr, dc in moves:

                newRow = row + dr
                newCol = col + dc

                # Check valid move
                if 0 <= newRow < 3 and 0 <= newCol < 3:

                    newPosition = newRow * 3 + newCol

                    # Create new state
                    newState = state.copy()

                    # Move blank tile
                    newState[blankPosition], newState[newPosition] = \
                        newState[newPosition], newState[blankPosition]

                    newStateTuple = tuple(newState)

                    # Add only if not visited
                    if newStateTuple not in visited:

                        newG = g + 1
                        newH = self.calculateHeuristic(newState)
                        newF = newG + newH

                        newPath = path + [newState]

                        openList.append(
                            (newF, newG, newState, newPath)
                        )

        print("No solution found.")

    # Calculate heuristic
    def calculateHeuristic(self, state):

        # Case 1: Number of Misplaced Tiles
        if self.heuristic == 1:

            count = 0

            for i in range(9):

                if state[i] != 0 and \
                   state[i] != self.environment.goalState[i]:
                    count += 1

            return count

        # Case 2: Manhattan Distance
        elif self.heuristic == 2:

            distance = 0

            for i in range(9):

                if state[i] != 0:

                    # Current position
                    currentRow = i // 3
                    currentCol = i % 3

                    # Goal position
                    goalPosition = \
                        self.environment.goalState.index(state[i])

                    goalRow = goalPosition // 3
                    goalCol = goalPosition % 3

                    distance += abs(currentRow - goalRow) + \
                                abs(currentCol - goalCol)

            return distance

        return 0

    # Function to print the puzzle
    def printState(self, state):

        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()



theEnvironment = Environment()


print("===== A* using Misplaced Tiles =====")
theAgent1 = AStarAgent(theEnvironment, 1)


print("===== A* using Manhattan Distance =====")
theAgent2 = AStarAgent(theEnvironment, 2)