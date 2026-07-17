import heapq

graph = {
    'S': [('A', 2), ('B', 4)],
    'A': [('C', 3), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 4)],
    'D': [('G', 2)],
    'G': []
}

def ucs(start, goal):

    pq = [(0, start, [])]
    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        path = path + [node]

        if node == goal:
            print("Shortest Path :", " -> ".join(path))
            print("Minimum Cost :", cost)
            return

        for neighbour, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, neighbour, path))


ucs('S', 'G')