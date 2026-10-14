from src.Robot_arm import RobotArm
robot1 = RobotArm(10, 8, 50, 30)
robot2 = RobotArm(5, 4, 60, 90)
print(robot1.joint1_angle)  # Output: 50
print(robot2.joint1_angle)  # Output: 60
robot1.joint1_angle = 70
print(robot1.joint1_angle)  # Output: 70
robot2.joint1_angle = 60
print(robot2.joint1_angle)  # Output: 60