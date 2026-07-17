class MarsRover:

    def move(self):
        print("Moving Forward")

    def capture_image(self):
        print("Capturing Image")

    def collect_sample(self):
        print("Collecting Soil Sample")

    def analyze_sample(self):
        print("Analyzing Sample")

    def avoid_obstacle(self):
        print("Obstacle Detected - Turning")

    def send_data(self):
        print("Sending Data to Earth")


rover = MarsRover()

rover.move()
rover.capture_image()
rover.collect_sample()
rover.analyze_sample()
rover.avoid_obstacle()
rover.send_data()