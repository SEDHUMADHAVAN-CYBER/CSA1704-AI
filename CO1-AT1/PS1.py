from collections import deque
#Breadth-First Search (BFS)

#Intelligent Search
#State Space Search
#Goal-Based Problem Solving
CAPACITY = (4, 3)
GOAL = 2

def get_next_states(state):
    x, y = state
    next_states = []

    # Fill jugs
    next_states.append((4, y))
    next_states.append((x, 3))

    # Empty jugs
    next_states.append((0, y))
    next_states.append((x, 0))

    # Pour 4 -> 3
    transfer = min(x, 3 - y)
    next_states.append((x - transfer, y + transfer))

    # Pour 3 -> 4
    transfer = min(y, 4 - x)
    next_states.append((x + transfer, y - transfer))

    return next_states

def bfs():
    queue = deque([((0, 0), [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state[0] == GOAL:
            print("Goal Found!")
            print("Solution Path:", path)
            return

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path))

bfs()