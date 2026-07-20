import heapq
#Uniform Cost Search (UCS)

#Uniform Cost Search
#Path Finding
#Cost-Based Decision Making
graph = {
    "S":[("A",2),("B",5)],
    "A":[("C",4),("D",7)],
    "B":[("D",1)],
    "C":[("G",3)],
    "D":[("G",2)],
    "G":[]
}

def uniform_cost_search(start, goal):

    frontier = [(0, start, [])]

    explored = set()

    while frontier:

        cost, node, path = heapq.heappop(frontier)

        if node in explored:
            continue

        explored.add(node)

        path = path + [node]

        if node == goal:

            print("Optimal Path:", path)
            print("Total Cost:", cost)
            return

        for neighbour, weight in graph[node]:

            if neighbour not in explored:

                heapq.heappush(frontier,
                               (cost+weight,
                                neighbour,
                                path))

uniform_cost_search("S","G")