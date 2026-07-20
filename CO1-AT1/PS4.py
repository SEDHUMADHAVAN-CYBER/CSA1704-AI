class CabAgent:
#Goal-Based Agent

#goal-Based Agent
#Decision Making
#Rule-Based Selection
    def __init__(self):

        self.cabs = {
            "Micro":120,
            "Mini":160,
            "Sedan":250,
            "Prime":350
        }

    def perceive(self):

        destination = input("Destination : ")
        budget = int(input("Budget : "))

        return destination, budget

    def think(self, budget):

        possible = []

        for cab, fare in self.cabs.items():
            if fare <= budget:
                possible.append((cab, fare))

        if possible:
            return min(possible, key=lambda x:x[1])

        return None

    def act(self, result):

        if result:
            print("Recommended Cab:", result[0])
            print("Fare:", result[1])
        else:
            print("No Cab Available")


agent = CabAgent()

destination, budget = agent.perceive()

choice = agent.think(budget)

agent.act(choice)