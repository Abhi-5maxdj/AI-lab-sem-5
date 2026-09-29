class Environment:
    def __init__(self):
        self.initialState = [1, 2, 3,
                             4, 0, 6,
                             7, 5, 8]

        self.goalState = [1, 2, 3,
                          4, 5, 6,
                          7, 8, 0]


class DFSAgent:
    def __init__(self, environment):

        self.environment = environment

        self.visited = set()

        self.path = []

        print("Initial State:")
        self.printState(environment.initialState)

        if self.dfs(environment.initialState):
            print("Goal State Reached!")
            print("\nSolution Path:")

            for state in self.path:
                self.printState(state)
        else:
            print("No solution found.")

    def dfs(self, state):

        stateTuple = tuple(state)

        if stateTuple in self.visited:
            return False

        self.visited.add(stateTuple)

        self.path.append(state)

        if state == self.environment.goalState:
            return True

        blankPosition = state.index(0)

        row = blankPosition // 3
        col = blankPosition % 3

        moves = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        for dr, dc in moves:

            newRow = row + dr
            newCol = col + dc

            if 0 <= newRow < 3 and 0 <= newCol < 3:

                newPosition = newRow * 3 + newCol

                newState = state.copy()

                newState[blankPosition], newState[newPosition] = \
                    newState[newPosition], newState[blankPosition]

                if self.dfs(newState):
                    return True

        self.path.pop()

        return False

    def printState(self, state):

        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()


theEnvironment = Environment()

theAgent = DFSAgent(theEnvironment) 