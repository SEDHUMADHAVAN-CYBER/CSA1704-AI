from collections import deque

def water_jug():
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (jug4, jug3), path = queue.popleft()

        if (jug4, jug3) in visited:
            continue
        visited.add((jug4, jug3))

        path = path + [(jug4, jug3)]

        if jug4 == 2:
            print("Solution:")
            for state in path:
                print(state)
            return

        next_states = [
            (4, jug3),                          # Fill 4-gallon jug
            (jug4, 3),                          # Fill 3-gallon jug
            (0, jug3),                          # Empty 4-gallon jug
            (jug4, 0),                          # Empty 3-gallon jug
            (jug4 - min(jug4, 3-jug3), jug3 + min(jug4, 3-jug3)),  # 4 -> 3
            (jug4 + min(jug3, 4-jug4), jug3 - min(jug3, 4-jug4))   # 3 -> 4
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

water_jug()