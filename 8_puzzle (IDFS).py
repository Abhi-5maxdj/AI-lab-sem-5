# IDDFS for 8-Puzzle

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)   
# 0 represents the blank tile


def get_neighbors(state):
    """Generate all valid moves of the blank tile."""
    neighbors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3


    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col


            new_state = list(state)
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


def depth_limited_dfs(state, depth, path, visited):
    """Depth-Limited DFS used by IDDFS."""


    path.append(state)


    if state == GOAL_STATE:
        return True


    if depth == 0:
        path.pop()
        return False


    visited.add(state)


    for new_state in get_neighbors(state):


        if new_state not in visited:

            if depth_limited_dfs(
                new_state,
                depth - 1,
                path,
                visited
            ):
                return True
    path.pop()

    return False


def iddfs(initial_state):
    """Iterative Deepening DFS."""

    depth = 0

    while True:

        path = []
        visited = set()

        if depth_limited_dfs(
            initial_state,
            depth,
            path,
            visited
        ):
            return path

        depth += 1


def print_state(state):
    """Print the puzzle state."""

    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()



initial_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

solution = iddfs(initial_state)

print("Solution found!")
print("Number of moves:", len(solution) - 1)
print()

for step, state in enumerate(solution):
    print("Step", step)
    print_state(state)
