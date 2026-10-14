import unittest
from src.Robot_arm import RobotArm
class TestRobotArm(unittest.TestCase):
    def test_initial_joint_angles(self):
        robot = RobotArm(10, 8, 30, 45)
        self.assertEqual(robot.joint1_angle, 30)
        self.assertEqual(robot.joint2_angle, 45)


    def test_independent_robot_states(self):
        robot1 = RobotArm(10, 8, 30, 45)
        robot2 = RobotArm(5, 4, 60, 90)
        self.assertEqual(robot1.joint1_angle, 30)
        self.assertEqual(robot2.joint1_angle, 60)
        robot1.joint1_angle = 70
        self.assertEqual(robot1.joint1_angle, 70)
        self.assertEqual(robot2.joint1_angle, 60)