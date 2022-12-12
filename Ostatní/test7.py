class Robot:
    def __init__(self, battery, height, color, max_travel_speed):
        self.battery = battery
        self.height = height
        self.color = color
        self.max_travel_speed = max_travel_speed

robot1 = [Robot(72, 1.5, "White-Black", 28)]
robot2 = [Robot(48, 1.0, "Green-Yellow", 32)]
robot3 = [Robot(64, 2.2, "Red-White", 12)]
robot4 = [Robot(24, 1.2, "Black-Blue", 16)]
robot5 = [Robot(72, 2.0, "Pink-White", 10)]
robot6 = [Robot(128, 1.8, "Orange-Green", 38)]

all_robots = robot1 + robot2 + robot3 + robot4 + robot5 + robot6

for robot in all_robots:
    print(f"Kapacita baterie {robot.battery} h\n"f"Výška {robot.height} m\n"f"Barva {robot.color}\n"f"Maximální rychlost {robot.max_travel_speed} km/h")
    print()


