class MarsRoverAgent:
#Model-Based Goal Agent
#Perceive → Think → Act

#Intelligent Agent
#Model-Based Agent
#Decision Making
    def __init__(self):
        self.goal = "Collect Rock Sample"

    def perceive(self):
        return {
            "rock": True,
            "obstacle": False,
            "battery": 90
        }

    def think(self, percept):
        if percept["battery"] < 20:
            return "Recharge"

        if percept["obstacle"]:
            return "Avoid Obstacle"

        if percept["rock"]:
            return "Collect Sample"

        return "Move Forward"

    def act(self, action):
        print("Agent Action:", action)


agent = MarsRoverAgent()

percept = agent.perceive()

decision = agent.think(percept)

agent.act(decision)